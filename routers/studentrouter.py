from fastapi import APIRouter, Response
from controller.studentcontroller import (
    create_students_controller,
    get_students_all_controller,
    get_students_controller,
    updateStudents_controller,
    deleteStudents_controller
)
from model.studentModel import Student

srouter = APIRouter(
    prefix="/students",
    tags=["students"]
)


@srouter.post('/poststudent')
def create_students(student: Student, response: Response):
    return create_students_controller(student, response)


@srouter.get('/getall')
def get_students_all(response: Response):
    return get_students_all_controller(response)


@srouter.get('/getstudent/{studentid}')
def get_students(studentid: int, response: Response):
    return get_students_controller(studentid, response)


@srouter.put('/updatestudent/{studentid}')
def updateStudents(studentid: int, student: Student, response: Response):
    return updateStudents_controller(studentid, student, response)


@srouter.delete('/deletestudent/{studentid}')
def deleteStudents(studentid: int, response: Response):
    return deleteStudents_controller(studentid, response)
