NO=input("Enter Two Integer Number and Two Decimal Number\n")

a1,a2,f1,f2=NO.split()
a1,a2=int(a1),int(a2)

f1,f2=float(f1),float(f2)

x=[a1,a2,f1,f2]
for i in range(0,4,2):
    x1,x2=x[i],x[i+1]
    print()
    print(f"Arithmetic Operation between {x1} and {x2}")
    print(f"Addition:\t{x1+x2}\nSubtraction:\t{x1-x2}\nMultiplication:\t{x1*x2}\nDivision:\t{(x1/x2):.2f}\nRemainder:\t{x1%x2:.1f}")
    
