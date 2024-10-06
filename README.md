# cel

## assumptions


## how to build

to build and run locally:

set a venv
python -m venv ./venv

activate a venv
source ./venv/bin/activate

install dependencies
pip install --no-cache-dir --upgrade -r ./requirements.txt

to run both from a shell (then you have to hunt and kill them from ps -af)
bash starter.sh

run each, including running fafstapi in dev mode so it watches for changes
fastapi dev main.py
python weatherFetch.py

## containerizaiton

to build and run docker container locally
docker build -t cel .
docker run -p 8000:8000 cel 


to get a command line on the running docker image
get the running image hash from
docker ps
then put the hash:
docker exec -it 83512586a08e /bin/bash


## interacting with the app
example end point call
http://localhost:8000/forcastRange?lat=39.7456&lng=-97.0892&dt=2024-10-05&hr=20

fastapi creates openAPI docs for endpoints:
http://localhost:8000/docs