# docker-from-omero-poc
 proof-of-concept running docker container from omero web
 
# PLEASE READ THIS FIRST
**Use this at your own risk, and only if you know exactly what you're doing.** If you're in doubt about the consequences of running docker as the OMERO user, please reach out to us. Even though we think there are no security issues in doing so, it is very easy to think about scenarios where there ARE issues if this is misused. 

This repo is intended purely as an example and as a starting point for anyone wanting to run analyses in Docker from OMERO.web. It is NOT to be used as a ready, polished product.

# How-to
- Edit `test_script.py` so that the `BaseClient` is created pointing to the correct hostname
- Build the Dockerfile in your server (I used `docker build -t test-omero .` from the repo directory)
- If you built it using a different container name, edit it on `omero_post_kvpair.py` so that docker runs the correct container
- Upload `omero_post_kvpair.py` as an OMERO script (`omero script upload omero_post_kvpair.py --official)`
- Make sure your OMERO user can run docker (it might need to be added to the `docker` group on your Linux system)
