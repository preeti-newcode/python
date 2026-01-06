n,m=map(int,input("Enter 2 no (eg, 40 10)\n:").split())
l=[]
for x in range(2,min([n,m])+1):
    if n%x==0 and m%x==0:
        l.append(x)

if len(l)>=1:
    print(f"Greatest Common Divisor of {n} and {m} is {max(l)}")
else:
    print(f"Greatest Common Divisor of {n} and {m} is 1")
