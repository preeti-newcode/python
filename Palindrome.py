#Palindrome Checker
value=input("Enter :")
size=len(value)
for x in range(size//2):
    if value[x]!=value[size-1-x]:
        print(value,"is not Palindrome")
        break;
else:
    print(value,"is Palindrome")
