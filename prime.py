#Prime
number=int(input("Enter : "))

for x in range(2,number):
    if number%x==0:
        print(number,"is not a prime number")
        break;
else:
    print(number,"is a prime number")
