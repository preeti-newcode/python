#factorial
number=int(input("Enter a number to see its factorial:"))
result=1
if number>1:
    for x in range(number,1,-1):
        result=result*x
    
print("Factorial of",number,"is",result)
