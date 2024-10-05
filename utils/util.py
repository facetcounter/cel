import sqlite3
from sqlite3 import Error

config = {
    "dbPath": "./db/db.sqlite",
    "logPath": "./logs/",
    "lat": 39.7456,
    "lng": -97.0892
}

def dbConnect():
    connection = None
    try:
        connection = sqlite3.connect(config["dbPath"])
        connection.set_trace_callback(log)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def log(msg):
    logFile = open(config["logPath"]+"logs.txt", "a")  # append mode
    logFile.write(msg+"\n")
    logFile.close()
    return

def dump(name,contents):
    logFile = open(config["logPath"]+name, "w")  # write mode
    logFile.write(contents)
    logFile.close()
    return

