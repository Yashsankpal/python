
def yesno(num,word):
    alpha = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    y = {}
    for i in word:
        if i in y.keys():
            y[i]=y[i]+1 
        else:
            y.update({i:1})
    print(y)
    x=[]
    for a,b in y.items(): 
       for i in range(1,b+1):
             x.append(alpha[a]*i)
    print(x)
    y=["Yes" if i in x else "No" for i in num]
    print(y)
word=list(input("Enter the word: "))
print(word)
num=list(map(int,input("Enter the num: ").split()))
print(num)
yesno(num,word)