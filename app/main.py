# author: Denem Orhun
# version: 
# date modified: 08/24/2020

'''
Using your favorite language (Go, Python, Java, Scala, Bash, etc.), create a hello world web application API that listens on port 8080 and greets a user with Hello! and exposes a health status endpoint.

Application url should return a greeting such as Hello! as json or plain text (ex: when you open a browser and navigate to http://localhost:8080, it should return Hello! plain text.)
Application should provide a health endpoint (http://localhost:8080/healthz) that returns HTTP status (200 OK) which indicates health of the application and returns a valid json with the following information:
status: status of the app: online, success, OK, error, etc.
version: running application version (ex: 0.0.1)
uptime: time duration or time stamp since the app is running (ex: running since YYYY-MM-DD hh:mm:ss) Example: When you open a browser and navigate to http://localhost:8080/healthz it should return:
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
            "status": 200,
            "Server running since:":server_start_time.strftime("%m/%d/%Y, %H:%M:%S"),
            "Uptime in seconds":time_running.seconds,
            "Version":version
            }
