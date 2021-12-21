# docker-from-omero-poc
 proof-of-concept running docker container from omero web

# How-to
- Edit `test_script.py` so that the `BaseClient` is created pointing to the correct hostname
- Build the Dockerfile in your server (I used `docker build -t test-omero .` from the repo directory)
- If you built it using a different container name, edit it on `omero_post_kvpair.py` so that docker runs the correct container
- Upload `omero_post_kvpair.py` as an OMERO script (`omero script upload omero_post_kvpair.py --official)`
- Make sure your OMERO user can run docker (it might need to be added to the `docker` group on your Linux system)