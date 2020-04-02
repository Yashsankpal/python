#1
def sortf(x):
    x.sort()
    y=[]
    while x[-1][0] != len(y):
        y.append([])
    for i in x:
        y[i[0]-1].append(i)
    return y

def hup(x,y):
    a=[]
    for i in x:
        if i[-1]-1 < len(y):
            for z in y[i[-1]-1]:
                if  i[0] != z[-1]:
                    a.append((i[0],z[-1]))
    return a

def hop(x):
    a=[]
    y=sortf(x)
    for i in y:
        a.extend(hup(i,y))
        
    #a=removedup(a)
    print(a)

    
x=[(1,2),(3,4),(5,6)]

hop(x)

#2
def valley(x):
    y=x.index(min(x))
    val_size=0
    i=1
    while y+i < len(x):
        if x[y-i] == x[y+i]:
            val_size+=1
        i+=1
    if val_size >= 2:
        print(True)
    else:
        print(False)

valley([3,3,2,1,2])

#3
def maxcount(x):
    y={}
    for i in x:
        if i in y.keys():
            y[i] = y[i] + 1
        else:
            y.update({i:1})
    return max(y.values())
print(maxcount([1,17,31,17,22,17]))

#4
def sublist(l1, l2):
    if l1==[]:
        return True
    elif l2==[]:
        return False
    else:
        for i in range(0, len(l2)):
            if l2[i] == l1[0]:
                f = 0
                for j in range(0, len(l1)):
                    if l1[j] != l2[i+j]:
                        f = 1
                        break
                if f==0:
                    break
        
        if f==0:
            return True
        else:
            return False

print(sublist([2,2,3],[2,2,3,4,5]))

print(sublist([2,2,4],[2,2,3,4,5]))

#5
def _(x):
    y=len(x)//2
    return x[y:]+x[:y]

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

x=_(lines)
for i in x:
    print(i)

#6
for i in range(101):
	print("Fizz"[i%3*4:]+"Buzz"[i%5*4:] or i)