def Natural(a):
    if a==1:
        return 1
    else:
        return a + Natural(a-1)

n=int(input("Total elements:"))
print(Natural(n))
