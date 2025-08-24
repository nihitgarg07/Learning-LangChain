from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# Inheriting base
class Student(BaseModel):
    name : str = 'nitish' # setting default value
    age : Optional[int] = None # Need to set None if Want to mark optional
    email: EmailStr # Validating using pydantic[email],
    cgpa : float = Field(gt=0,lt=10,default=5,description="A decimal value representing the CGPA of the student") # Setting Constrant of CGPA as float and setting value greater than =0 and less than equal to 10

new_student ={
    'name' : 'Student',
    'age': 32,
    'email':'abc@gmail.com' ,
    'cgpa': 9
    
}

student = Student(**new_student)

print(student)
student_dict = dict(student)
print(student_dict)
student_json = student.model_dump_json()
print(student_json)
