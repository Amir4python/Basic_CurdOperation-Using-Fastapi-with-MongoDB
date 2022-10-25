#we write logic 
from fastapi import APIRouter
from models.students import Student
from config.database import connection
from schemas.students import studentEntity,studentEntityList
from bson import ObjectId
student_router=APIRouter()

@student_router.get('/hello')
async def helloworld():
  return "Hello World AMIR"
#get the students list
@student_router.get('/students')
async def find_all_students():
  return studentEntityList(connection.local.student.find())

#adding student record
@student_router.post('/students')
async def add_student(student:Student):
  connection.local.student.insert_one(dict(student))
  return studentEntityList(connection.local.student.find())

#updating th student
@student_router.put('/students/{studentID}')
async def update_student(studentID,student:Student):
  connection.local.student.find_one_and_update(
    {"_id":ObjectId(studentID)},
    {"$set":dict(student)}
  )
  return studentEntity(connection.local.student.find_one({"_id":ObjectId(studentID)}))

#deleting the student 
@student_router.delete('/students/{studentID}')
async def delete_student(studentID):
  
  return studentEntity(connection.local.student.find_one_and_delete({"_id":ObjectId(studentID)}))

#finding the student by id 
@student_router.get('/students/{studentID}')
async def find_student_by_id(studentID):
  
  return studentEntity(connection.local.student.find_one({"_id":ObjectId(studentID)}))
