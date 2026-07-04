from sqlalchemy.orm import Session
import models
import schemas

# Create a new student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Get all students
def get_students(db: Session):
    return db.query(models.Student).all()

# Get one student by ID
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

# Update a student
def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = get_student(db, student_id)

    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.course = student.course
        db.commit()
        db.refresh(db_student)

    return db_student

# Delete a student
def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)

    if db_student:
        db.delete(db_student)
        db.commit()

    return db_student