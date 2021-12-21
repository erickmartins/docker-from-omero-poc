import subprocess
import docker
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
            "Value", grouping="3",
            description="Value for the map annotation to be added", 
            optional=False)
    )

    id = client.getSessionId()
    try:
        # either version works fine - right now I have docker-py but 
        # if you don't want the extra dependency subprocess is fine
        scriptParams = client.getInputs(unwrap=True)
        # docker_cmd = ['docker', 'run', 'test-omero', id, 
        #              str(scriptParams)]
        # process = subprocess.Popen(docker_cmd,
        #                            stdout=subprocess.PIPE,
        #                            stderr=subprocess.PIPE
        #                           )
        # stdoutval, stderrval = process.communicate()
        # stdoutval, stderrval = stdoutval.decode('UTF-8'), stderrval.decode('UTF-8')
        args = [id, str(scriptParams)]
        dock = docker.from_env()
        dock.containers.run("test-omero", args)
        

    finally:
        client.closeSession()

if __name__ == '__main__':
    runScript()