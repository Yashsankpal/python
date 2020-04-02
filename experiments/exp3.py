def blah(x):
    x.sort(key = lambda x: x[len(x)-1])

x = [(1,2),(7,2,6),(4,6,9),(2,3,1)]
blah(x)
print(x)

y = {}
a = input("enter the string: ")

for i in a:
    if i in y.keys():
        y[i] += 1
    else:
        y.update({i:1})

for a,b in y.items():
    if b == 1:
        print(a,end = " ")
print()
a = list(input("enter the string: ").split(','))

x = ""
for i in a:
    if len(x) < len(i):
        x = i

print(x)