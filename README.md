# cel

## assumptions

I assumed that the overall purpose of the application was to allow analysis of how much the foraast for a given day/time and location would vary over the preceding three days.

I don't think collecting data more frequently changes this result.  I think querying into which hour of a 24 hour period has the biggest variance miught be interesting.

In implementation, I assumed that less code, fewer dependencies and fewer files would be more readable for a simple implementation so I stayed with vanilla python wherever I could.  I also wrote the minimum code needed to solve the problem, omitting error checking and test automation.

I assumed that fastapi was a good choice for implementing this with, as opposed to a more opinionated and more boilerplate heayv framework.  Were the application to grow more complex it may make sense to use one of the other python web frameworks.





## to do list
If the assumption about the purpose of the data collection is correct, an second table could be created for past data holding only the derived aggregations we care about and keeping the data size down were we to have a lot of data and a lot of requests from end users.

I would attach storage for the sqlite and logs instead of having them live in the container when they reset when the container restarts. That said, having a standalone DB and structlog sending to a log aggregation system would be the better long term solution.

Both the fastapi application and the polling data collection application live in the same container.  Once data and logs were taken out into external systems, it would be easy to make one container for each process.

Simple test automation would be helpful, and integrating test automation runs into the deploy process would be good.

Some error conditions may kill the application so being a bit thorough about testing edge cases and also setting up health checks and auto-restarts would be good.




## how to build

to build and run locally:

set a venv
```
    python -m venv ./venv
```

activate a venv
```
    source ./venv/bin/activate
```

install dependencies
```
    pip install --no-cache-dir --upgrade -r ./requirements.txt
```

to run both from a shell (then you have to hunt and kill them from ps -af)
```
    bash starter.sh
```

run each, including running fafstapi in dev mode so it watches for changes
```
    fastapi dev main.py
    python weatherFetch.py
```

## containerizaiton

to build and run docker container locally
```
    docker build -t cel .
    docker run -p 8000:8000 cel 
```

to get a command line on the running docker image
get the running image hash from
```
    docker ps
```
then put the hash:
```
    docker exec -it 83512586a08e /bin/bash
```

## interacting with the app
example end point call
```
    http://localhost:8000/forcastRange?lat=39.7456&lng=-97.0892&dt=2024-10-05&hr=20
```

fastapi creates openAPI docs for endpoints:
```
    http://localhost:8000/docs
```