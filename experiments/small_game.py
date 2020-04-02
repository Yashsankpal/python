import random
def guess(x,y):
    x = [i for i in str(x)]
    y = [i for i in str(y)]
    
    if x == y:
        return 0
    elif x[0] == y[0] or x[1] == y[1] or x[2] == y[2]:
        return 1
    else:
        return -1    

def __init__():
    print("Number is selected enter your guess: ")
    x = int(input("Enter the guess value: "))
    y = random.randint(100,999)

    while(True):
        if guess(x,y) == 0:
            print("Find match")
            break
        elif guess(x,y) == 1:
            print("Match")
        else:
            print("Not found")
        x = int(input("Enter the guess value: "))
        

__init__()