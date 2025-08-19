from typing import TypedDict

class Person(TypedDict):
    name:str
    age: int


new_person: Person = {'name':'Nihit','age':27}

print(new_person)