#linear search

def linSearch(no,List):
    a=List
    for x in range(len(a)):
        if a[x]==no:
            return x
    else:
        return -1

conti=1
while conti:
    size=int(input("Enter size of a list you want:"))
    l=[]
    for x in range(size):
        a=int(input())
        l.append(a)
    value=int(input("Enter data to find:"))
    result=linSearch(value,l)
    if result==-1:
        print(value,"is not present in given List")
    else:
        print(value,"is in",result,"index")
    conti=int(input("\nIf you want to continue press 1:"))
    if conti!=1:
        break
print("Thank You :)")
    
