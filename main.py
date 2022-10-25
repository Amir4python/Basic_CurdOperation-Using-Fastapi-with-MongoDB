#importing fastapi
from fastapi import FastAPI

from routes.students import student_router
#create app
app=FastAPI()

app.include_router(student_router)