import schedule
import time
import datetime
import requests
import json
from utils.util import dbConnect,log,dump,config



conn = dbConnect()

def job():
    print("running job...")
    url = "https://api.weather.gov/points/"+str(config["lat"])+","+str(config["lng"])
    log ("fetching: "+ url)
    response = requests.get(url)
    data = response.json()
    dump("station.json",json.dumps(data))
    hourlyUrl = data["properties"]["forecastHourly"]
    log ("fetching: "+ hourlyUrl)
    response = requests.get(hourlyUrl)
    data = response.json()
    dump("weather.json",json.dumps(data))    
    insertQuery = "insert into predictedTemps (capturedTime, predictionTime, predictedTemp, lat,lng) values (?,?,?,?,?)"
    for i in range(72):
        conn.execute(insertQuery, (
            datetime.datetime.now(),
            data["properties"]["periods"][i]["startTime"],
            data["properties"]["periods"][i]["temperature"],
            config["lat"],
            config["lng"]
        ))
        conn.commit()
    print("job done")
        


def announce():
    print("Waiting to run job...")

schedule.every(10).seconds.do(announce)
# schedule.every().hour.do(job)
schedule.every(10).minutes.do(job)

job()
while 1:
     schedule.run_pending()
     time.sleep(1)