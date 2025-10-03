#check number of character
name=input("Enter your name:").split()
series=''.join(name)
if len(series)<10:
    print("Less than 10 characters")
else:
    print("More than or equal to 10 characters")
