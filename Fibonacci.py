#Fibonacci Sequence
number=int(input("Enter a number:"))
l=list([0,1])
for x in range(number-2):
        l.append(l[-1]+l[-2])
print(l)
