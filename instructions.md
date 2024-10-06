# BACKEND SOFTWARE ENGINEER AT HOME CODING CHALLENGE 

Please spend no more than 4 hours on this exercise. If you have any questions, please reach out to the recruiter at CEL for assistance. 

## INSTRUCTIONS 

Implement a Dockerized application in Python that tracks the variation in weather temperature forecasts overtime for a given location using the weather.gov API and a local data store. 

### REQUIREMENTS 

1. As an input, the application must accept a configurable location for which to track weather forecasts, specified as a latitude and longitude, for example: 

```json
{
    "location": { 
        "lat": "39.7456", 
        "lon": "-97.0892" 
    } 
} 
```

2. At a configurable interval, defaulting to 60 minutes, the application must query the API described at https://www.weather.gov/documentation/services-web-api to retrieve forecast data for the specified latitude and longitude 

3. The application must store the set of hourly temperature forecasts for the next 72 hours, as predicted at the time of retrieval, in a local datastore. 

4. The application must expose an API or endpoint that accepts as inputs: a latitude, longitude, date, and UTC hour of day (0-23) 

5. The API or endpoint must return the highest and lowest recorded forecast in the database for the specified location, day and hour of day

6. The application must contain an appropriate Dockerfile and other resources to containerize the application 

7. The application must include a README with instructions for building the Docker container and running the application 

8. Clearly state all of the assumptions you made in completing the application