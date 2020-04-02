
class Student:
    grade = ""
    def __init__(self,roll_no,name,score):
        self.roll_no = roll_no
        self.name = name
        self.score = score
    def grde(self):
        x = ""
        if sum(self.score) >= 80.00:
            x = "A"
        elif sum(self.score) >= 60.00:
            x = "B"
        elif sum(self.score) >= 50.00:
            x = "C"
        else:
            x ="F"
        self.grade = x


def inx():
    name = input("Enter the name: ")
    roll_no = input("Enter the roll_call: ")
    score = list(map(int,input("Enter the marks: ").split()))
    stu = Student(roll_no,name,score)
    stu.grde()
    print(f"Student: {stu.name} Roll_no: {stu.roll_no} Grade: {stu.grade}")

print("Code started")

while(True):
    inx()
    x = input("wanna continue? Y/N: ")
    if x == 'n' or x == 'N':
        break
