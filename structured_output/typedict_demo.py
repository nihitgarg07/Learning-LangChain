from typing import TypedDict


# Inheriting typeDict and Creating a blueprint for Dict
class Person(TypedDict):
    name:str
    age: int


# Creating an object person and save it in variable
new_person: Person = {'name':'Nihit','age':27}

print(new_person)