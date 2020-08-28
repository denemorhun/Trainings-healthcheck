# author: Denem Orhun
# date modified: 08/28/2020

'''
Basic app that returns the health of an endpoint. 

Open a browser and navigate to http://localhost:8080/healthz it should return:
{
  "status": "OK",
  "version": "0.0.1",
  "uptime": "up since 2020-08-04 08:00:05"
}
'''

import uvicorn

from fastapi import FastAPI, status

from datetime import timedelta
import datetime

from pydantic import BaseModel

import os, sys

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")

server_start_time = datetime.datetime.now()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.get("/healthz")
def get_health():
    # calculate server uptime
    time_running = datetime.datetime.now() - server_start_time

    # read version from file
    fp = open(os.path.join(sys.path[0], "VERSION"))
    version = fp.readline()
    return {
            "status": status.HTTP_200_OK,
            "Server running since:":server_start_time.strftime("%Y/%m/%d, %H:%M:%S"),
            "Uptime in seconds":time_running.seconds,
            "Version":version
            }
