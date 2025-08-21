#factors 
number=int(input("Enter a number to find its factorial:"))
fact=[1]
x=2
while number>x:
    if number%x==0:
        fact.append(x)
    x+=1
fact.append(number)
print("Factorial of",number,"is",fact)
