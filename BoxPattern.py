no=int(input("Number of rows:"))
for x in range(1,no+1):
    if x in [1,no]:
        print("*"*no)
    else:
        for i in range(no):
            if i==0 or i==no-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
