def Table(a):
    for x in range(1,11):
        print(f"{a} X {x} = {a*x}")

n=int(input("Enter a number to print its table:"))
Table(n)
