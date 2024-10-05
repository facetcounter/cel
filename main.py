from fastapi import FastAPI
from datetime import datetime, timedelta
from utils.util import dbConnect,log
app = FastAPI()

conn = dbConnect()
cur = conn.cursor()

@app.get("/")
async def root():
    conn.execute("update connectionLog set ct = ct + 1 where id = 1")
    conn.commit()
    count = cur.execute("SELECT ct FROM connectionLog WHERE id = 1")
    records = count.fetchall()
    return {"message": "Hello World: "+str(records[0][0])}

@app.get("/forcastRange")
async def forcastRange(lat: float=39.7456, lng: float = -97.0892, dt:str="",hr:int=12):
    predictionStartTime = datetime.strptime(dt+" "+str(hr)+":00:00", "%Y-%m-%d %H:%M:%S")
    predictionEndTime = predictionStartTime + timedelta(hours=1)
    cur.execute("SELECT max(predictedTemp),min(predictedTemp) FROM predictedTemps where lat = ? and lng = ? and predictionTime > ? and predictionTime < ?", (lat, lng, predictionStartTime.strftime("%Y-%m-%dT%H:%M:%S-00:00"), predictionEndTime.strftime("%Y-%m-%dT%H:%M:%S-00:00")))
    records = cur.fetchall()
    return {"message": records}