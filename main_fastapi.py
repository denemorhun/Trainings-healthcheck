# author: Denem Orhun
# version:
# date modified: 08/24/2020
 
# from typing import Optional
# from pydantic import BaseModel
import uvicorn

from fastapi import FastAPI, status
from enum import Enum

from datetime import timedelta
import datetime

import os, sys

app = FastAPI()

if __name__ == "__main__":
    os.system('ver up')
    uvicorn.run("main_fastapi:app", host="0.0.0.0", port=8080, log_level="info")

server_start_time = datetime.datetime.now()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def get_health():
    return {"status": 200}

@app.get("/time")
def get_uptime():
    time_running = datetime.datetime.now() - server_start_time
    return{"Uptime in seconds":time_running}

@app.get("/version")
def get_version():
    fp = open(os.path.join(sys.path[0], "VERSION"))
    version = fp.readline()
    return{"Version":version}
