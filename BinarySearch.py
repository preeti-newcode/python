from random import randint

def BinarySearch(x,l):
    left,right=0,len(l)-1
    while(left<=right):
        mid=(left+right)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            right=mid-1
        else:
            left=mid+1
    return -1

li=[randint(0,100) for _ in range(10)]
li.sort()

value=int(input("Enter a no.:"))


output=BinarySearch(value,li)
if output==-1:
    print("Data not found")
else:
    print(f"{value} is found at {output}th index")


