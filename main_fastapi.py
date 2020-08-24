from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, status
from enum import Enum

from datetime import timedelta
import datetime

app = FastAPI()

datetime_object = datetime.datetime.now()
print(datetime_object.strftime("%H:%M:%S"))


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def get_health():
    return {"status": 200}

@app.get("/time")
def get_uptime():

    time_running = datetime.datetime.now() - datetime_object
    # total_seconds = time_delta.total_seconds()
    # return{"uptime":time_running.strftime("%H:%M:%S")}

    # return{"uptime":total_seconds}
    return{"Uptime in seconds":time_running}

@app.get("/version")
