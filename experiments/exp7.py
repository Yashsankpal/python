
class Employee:
    def __init__(self,name,dai_sal):
        self.name = name
        self.sal = dai_sal

class Attendee:
    def __init__(self,name,dance):
        self.name = name
        self.attendance = dance


emp1 = Employee('Yash',1500)
emp2 = Employee('Rajan',10000)

atte1 = Attendee('Rajan',240)
atte2 = Attendee('Yash',120)


print(f"Salary of {emp1.name} is {emp1.sal*atte2.attendance}")
print(f"Salary of {emp2.name} is {emp2.sal*atte1.attendance}")

print(emp1.sal > emp2.sal)

print(emp1.sal+emp2.sal)