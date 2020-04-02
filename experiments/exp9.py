from faker import Faker
from random import randint
fake = Faker()
class DefaultError(Exception):
    pass
def defaultList(li):
    for i in li:
        try:
                if i.marks < 35:
                    raise DefaultError
        except DefaultError:
            print(f"{i.name} is in defaulter list !!")


class Student:
    def __init__(self,name,marks,attendance):
        self.name = name
        self.marks = marks
        self.attendance = attendance
    
li=[]
x=int(input('Enter no. of students: '))


for i in range(x):
    li.append(Student(fake.name(),randint(20,100),randint(200,300)))

defaultList(li)