from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Student Management API")

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Student
@app.post("/students", status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

# Get All Students
@app.get("/students")
def get_all_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

# Get Student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update Student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated = crud.update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

# Delete Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}