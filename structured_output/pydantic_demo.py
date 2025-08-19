from pydantic import BaseModel

# Inheriting base
class Student(BaseModel):
    name : str



new_student ={
    'name' : 'Student'
}

student = Student(**new_student)

print(student)