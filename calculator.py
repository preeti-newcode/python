#calculator

#function
def cal(no1,no2,sym):
    for x in sym:
        if x=='+':
            return no1+no2
        elif x=='-':
            return no1-no2
        elif x=="/":
            return no1/no2
        elif x=='*':
            return no1*no2
        else:
            break;
    else:
        return 'error'

conti=True
while conti:
    x=input("Enter 2 no. (10 2): ")
    sign=input("+   -   /   * :")
    n1,n2=x.split()
    n1,n2=int(n1),int(n2)

    result=cal(n1,n2,sign)
    print("Your Given Number:",n1,",",n2,"and symbol:",sign)
    print(result)
    print()
    
    conti=input("Want to continue:\nTrue\nFalse\n")
    if conti in ['0','false','FALSE','False']:
        break
print("Thanks :)")



