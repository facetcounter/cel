# cel

to build and run locally:
source ./venv/bin/activate
pip install --no-cache-dir --upgrade -r ./requirements.txt


to build and run docker container locally
docker build -t cel .
docker run -p 8000:8000 cel 


to get a command line on the running docker image
get the running image hash from
docker ps
then put the hash:
docker exec -it 83512586a08e /bin/bash



example end point call
http://localhost:8000/forcastRange?lat=39.7456&lng=-97.0892&dt=2024-10-05&hr=20

fastapi creates openAPI docs for endpoints:
http://localhost:8000/docs