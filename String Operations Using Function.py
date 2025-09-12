#function for swtich case
def Function(option,s1,s2):
    
    #repeated value
    s3=s1+" "+s2
    if option!=5:
        x=int(input(f"\nChoose 1)'{s1}' String\n2)'{s2}' String\n3)Both String\n"))
        if x==1:
            x=s1
        elif x==2:
            x=s2
        else:
            x=s3
    
    #Access Element
    if option==1:
        x1=int(input("Choose 1)Index Access\n2)Range Access\n"))
        if x1==1:
            x11=int(input("Enter : "))
            return x[x11]
        
        elif x1==2:
            x11=int(input("Stating value: "))
            x12=int(input("Stop value: "))
            return x[x11:x12]
    
    #Size
    elif option==2:
        return len(x)
    
    #Smallest and Largest value
    elif option==3:
        value=input("enter max/min\n").lower()
        if value=='max':
            return max(x)
        else:
            if x==s3:
                x=s1+s2
            return min(x)
    
    #Capitalize/Small letter
    elif option==4:
        way=int(input("1)Capital\t2)Small\n"))
        if way==1:
            return x.upper()
        else:
            return x.lower()
    
    #concatenation
    elif option==5:
        return s3
    
    #Replace
    elif option==6:
        value=input("Value to be replace: ")
        new_value=input("new value: ")
        x=x.replace(value,new_value)
        return x
        
    

#Main body
s=input("Enter two string separated by comma ")
s1,s2=s.split(",")
print("Options\n1:Access\n2:Size\n3:Smallest and Largest value\n4:Capitalize or small letter\n5:Join\n6:Replace\n7:Quit\n")
while True:
    choice=int(input("Enter your choice: "))
    
    if choice!=7:
        print(Function(choice,s1,s2))
    else:
        break
    
