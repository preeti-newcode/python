l=input("Enter no to check if its stisfy Armstrong rule:")
size=len(l)
l=int(l)
original=l

data=0
for x in range(size):
    data=data+((l%10)**size)
    l=l//10

if original==data:
    print(f"{original} is an Armstrong Number")
else:
    print(f"{original} is not an Armstrong Number")
    
