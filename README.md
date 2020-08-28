# Healthcheck Endpoint


Application url should return a greeting such as Hello:World on  as json when user opens a browser and navigates to http://localhost:8080,

Application should provide a health endpoint (http://localhost:8080/healthz) that returns HTTP status (200 OK) which indicates health of the application and returns a valid json with the following information:
- status: status of the app: online, success, OK, error, etc.
- version: running application version (ex: 0.0.1). Version is stored in a file within the package. 
- uptime: time duration or time stamp since the app is running (ex: running since YYYY-MM-DD hh:mm:ss) Example: When you open a browser and navigate to http://localhost:8080/healthz it should return something like:

{
    "status": 200,
    "Server running since:": "2020/08/28, 11:51:46",
    "Uptime in seconds": 380,
    "Version": "0.1.4"
}



