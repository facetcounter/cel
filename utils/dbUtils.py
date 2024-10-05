import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

conn = create_connection("./db/db.sqlite")

c1 = "create table connectionLog (id integer primary key, ct integer)"
c2 = "insert into connectionLog (id, ct) values (1, 0)"
c3 = "drop table connectionLog"

d1 = "create table predictedTemps (id integer primary key, capturedTime timestamp, predictionTime timestamp, predictedTemp float, lat float,lng float)"

try:
    conn.execute(d1)
    conn.commit()
except Exception as e:
    print(e)

