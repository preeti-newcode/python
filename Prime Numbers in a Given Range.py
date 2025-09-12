print("Enter range to find prime number between them")
x=int(input("Min value:"))
x2=int(input("Max value:"))
prime=[]

#Loop to find prime between given range
for a in range(x,x2+1):
    for b in range(2,a):
        if a%b==0:
            break;
    else:
        prime.append(a)

print(prime)
