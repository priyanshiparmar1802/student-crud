from fastapi import HTTPException
from models.student_model import Student


students = []


def create_student(student: Student):
    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student)
    return student


def get_all_students():
    return students


def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            updated_student.id = student_id
            students[index] = updated_student
            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )