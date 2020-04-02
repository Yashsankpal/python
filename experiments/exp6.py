import numpy as np

class MyMatrix:
    addit = False
    subt = False
    multi = False
    square = False
    
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        if x1 == x2 and y1 == y2:
            self.addit = True
            self.subt = True
        if y1 == x2:
            self.multi = True
        if x1 == y1:
            self.square = True

        self.x1,self.y1 = x1,y1
        self.x2,self.y2 = x2,y2
        self.a = np.random.randint(10,size = (x1,y1))
        self.b = np.random.randint(10,size = (x2,y2))

    def value(self):
         
        print(f"matrix a: {self.a}")
        print(f"matrix b: {self.b}")

    def add(self):
        if self.addit == True:
            x = np.add(self.a,self.b)
            print(f"Add a and b is : {x}") 
        else:
            print("Sorry operation not valid")

    def sub(self):
        if self.subt == True:
            x = np.subtract(self.a,self.b)
            print(f"subtract a and b is : {x}") 
        else:
            print("Sorry operation not valid")

    def mul(self):
        if self.multi == True:
            x = np.dot(self.a,self.b)
           # print(self.a,"\n\n",self.b)
            print(f"multiply a and b is : {x}") 
        else:
            print("Sorry operation not valid")

    def inv(self):
        if self.square == True:
            x = np.linalg.inv(self.a)
            print("Inverse of matrix: ",x)
        else:
            print("Sorry operation not valid")

            
class SubMatrix(MyMatrix):
    def __init__(self,x1,y1):    
        super(SubMatrix,self).__init__(x1,y1)

def __init__():
    x1,y1,x2,y2 = map(int,input("Enter the rows and columns as x1,y1,x2,y2: ").split())
    x = MyMatrix(x1,y1,x2,y2)
    x.add()
    x.sub()
    x.mul()
    x.value()
def sub():
    x1,y1 = map(int,input("Enter the rows and columns as x1,y1: ").split())
    x = SubMatrix(x1,y1)
    x.inv()
    x.value()

__init__()
sub()

