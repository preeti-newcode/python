def ITEMS(l,choice):
    #Access Items
    if choice==1:
        x=int(input("1)Index\n2)Range\n"))
        if x==1:
            x1=int(input("Index value:"))
            return l[x1]
        else:
            x1=int(input("Start value: "))
            x2=int(input("Stop value: "))
            return l[x1:x2]
            
    #Replace
    elif choice==2:
        x=int(input("Index value: "))
        x1=int(input("Value: "))
        l[x]=x1
        return l
    
    #Append    
    elif choice==3:
        x=int(input("New value to add: "))
        l.append(x)
        return l
    
    #Insert
    elif choice==4:
        x=int(input("New value to add: "))
        print(f"length of list {len(l)}")
        x1=int(input("poistion for new value"))
        l.insert(x1,x)
        return l
    
    #Extend
    elif choice==5:
        size=int(input("Size for new list: "))
        l2=[]
        for x in range(size):
            value=int(input())
            l2.append(value)
        l.extend(l2)
        return l
    
    #Remove
    elif choice==6:
        x=int(input("1)Remove last element\n2)Remove index value\n3)Remove value"))
        if x==1:
            l.pop()
            return l
        elif x==2:
            print("Length of List",len(l))
            indi=int(input("Enter index to remove:"))
            l.pop(indi)
            return l
        else:
            value=int(input("Value to remove: "))
            l.remove(value)
            return l
        
    #Clear list
    elif choice==7:
        l.clear()
        return l
            

#Main Body
size=int(input("Size of a list: "))
List=[]
for x in range(size):
    value=int(input())
    List.append(value)
    
print("Options:\n1)Access Item\n2)Replace Value\n3)Append\n4)Insert\n5)Extend\n6)Remove Value\n7)Clear List\n8Exist")
while True:
    option=int(input("Your choice: "))
    if option!=8:
        print(ITEMS(List,option))
    else:
        break
    
