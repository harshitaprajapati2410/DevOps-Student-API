from fastapi import Response
from model.studentModel import Student

students = []
id = 0


def get_students_all_controller(response: Response):
    print('Data-->', students)
    response.status_code = 200
    return {"message": "student get Successfully", "Students": students}


def create_students_controller(student: Student, response: Response):
    global id
    try:
        id += 1
        student.id = id
        students.append(student)
        response.status_code = 201
        return {
            "message": "student created Successfully",
            "student": student
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": str(e), "isSuccess": False}


def get_students_controller(studentid: int, response: Response):
    try:
        for student in students:
            if student.id == studentid:
                response.status_code = 200
                return {"message": student, "isSuccess": True}

        response.status_code = 404
        return {"message": "student Not found", "isSuccess": False}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": "Error Fetching student", "isSuccess": False}


def updateStudents_controller(studentid: int, student: Student, response: Response):
    try:
        for index in range(0, len(students), 1):
            if students[index].id == studentid:
                student.id = studentid
                students[index] = student
                response.status_code = 200
                return {
                    "message": "student updated Successfully",
                    "isSuccess": True
                }

        response.status_code = 404
        return {"message": "student Not found", "isSuccess": False}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": "Error Updating student", "isSuccess": False}


def deleteStudents_controller(studentid: int, response: Response):
    try:
        for student in students:
            if student.id == studentid:
                students.remove(student)
                response.status_code = 200
                return {
                    "message": "student deleted Successfully",
                    "isSuccess": True
                }

        response.status_code = 404
        return {"message": "student Not found", "isSuccess": False}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": "Error Deleting student", "isSuccess": False}
