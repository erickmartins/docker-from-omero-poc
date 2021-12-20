import subprocess
from omero import scripts
from omero.rtypes import rstring, rlong

def runScript():
    """
    The main entry point of the script
    """
    data_types = [rstring('Dataset'), rstring('Image'), rstring('Project')]

    client = scripts.client(
        'Example Docker Test', 'Example script using docker container',

        scripts.String(
            "Data_Type", optional=False, grouping="1",
            description="The data you want to work with.", values=data_types,
            default="Image"),
        scripts.List(
            "IDs", optional=False, grouping="1",
            description="List of Dataset IDs or Image IDs").ofType(rlong(0)),
        scripts.String(
            "Key", grouping="2",
            description="Key for the map annotation to be added", 
            optional=False),
        scripts.String(
            "Value", grouping="2",
            description="Value for the map annotation to be added", 
            optional=False)
    )

    id = client.getSessionId()
    try:
        scriptParams = client.getInputs(unwrap=True)
        docker_cmd = ['docker', 'run', 'test-omero', id, 
                     str(scriptParams)]
        process = subprocess.Popen(docker_cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                  )
        stdoutval, stderrval = process.communicate()
        stdoutval, stderrval = stdoutval.decode('UTF-8'), stderrval.decode('UTF-8')
        message = 'Params: %s\n' % scriptParams
        message = message + "ID: %s\n" % id
        message = message + "params type: %s\n" % str(type(scriptParams))
        print(message)
        client.setOutput('Message', rstring(str(message)))

    finally:
        client.closeSession()

if __name__ == '__main__':
    runScript()