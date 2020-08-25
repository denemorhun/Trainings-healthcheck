# Trainings/healthcheck

Anyone (or any build server) that receives a copy of the project needs only to run the command:

$ pip freeze > requirements.txt
 
# uvicorn main_fastapi:app --reload --port 8080 --host 0.0.0.0