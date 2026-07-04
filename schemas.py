from pydantic import BaseModel

# Data received when creating or updating a student
class StudentCreate(BaseModel):
    name: str
    age: int
    course: str

# Data returned by the API
class Student(StudentCreate):
    id: int

    class Config:
        from_attributes = True