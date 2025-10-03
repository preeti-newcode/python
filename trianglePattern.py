no=int(input("Number of rows:"))
for x in range(1,no+1):
    print(" "*(no-x),end="")
    print("*"*(2*x-1))
