#binary search

def biSearch(value,List):
    List.sort()
    a=List
    size=len(a)
    left=0
    right=size-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]==value:
            return mid
        elif a[mid]>value:
            right=mid-1
        elif a[mid]<value:
            left=mid+1
    return -1


size=int(input("Enter size of a list:"))
l=[]
for x in range(size):
    n=int(input())
    l.append(n)
while 1:
    value=int(input("Enter value to search:"))
    result=biSearch(value,l)
    if result==-1:
        print("Not Found")
    else:
        print("Found")
    conti=int(input("Press 1 for continue:"))
    if conti!=1:
        break;
print("Thank You")
