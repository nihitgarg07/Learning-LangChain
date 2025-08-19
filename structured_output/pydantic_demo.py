from pydantic import BaseModel

class Student(BaseModel):
    name : str



new_student ={
    'name' : 'Student'
}

student = Student(**new_student)

print(student)