from fastapi import APIRouter, status
from models.student_model import Student
from controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)


router = APIRouter()


@router.post("/students", status_code=status.HTTP_201_CREATED)
def create(student: Student):
    return create_student(student)


@router.get("/students")
def get_all():
    return get_all_students()


@router.get("/students/{student_id}")
def get_by_id(student_id: int):
    return get_student_by_id(student_id)


@router.put("/students/{student_id}")
def update(student_id: int, student: Student):
    return update_student(student_id, student)


@router.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(student_id: int):
    delete_student(student_id)