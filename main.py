from fastapi import FastAPI

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
cur = conn.cursor()
app = FastAPI()


@app.get("/")
async def root():
    conn.execute("update connectionLog set ct = ct + 1 where id = 1")
    conn.commit()
    count = cur.execute("SELECT ct FROM connectionLog WHERE id = 1")
    records = count.fetchall()
    print("records are ", records)
    return {"message": "Hello World: "+str(records[0][0])}
