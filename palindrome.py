#palindrome
a=input("Enter to check its palindrome nature")
size=len(a)
for i in range(size//2):
    if a[i]!=a[size-1-i]:
        print("Not a palindrome")
        break
else:
    print(a,"is a palindrome")
