'''
f. To Count the Frequency of Words Appearing in a String Using a Dictionary. 
'''

x = {i:i**2 for i in range(1,10)}
y = {i:i**2 for i in range(10,20)}
x.update(y)
print(x)

for i in sorted(x.keys(),reverse=True):
    print(i," = ",x[i])

print(sorted(list(set(i for i in x.values()))))

print(x[len(x)],"+",x[len(x)-1],"+",x[len(x)-2])

y = {}
x = input("Enter the string: ")

for i in str(x):
	if i in y.keys():
		y[i] = y[i] + 1
	else:
		y.update({i:1})
for a,b in y.items():
	print(a," = ",b,"")

