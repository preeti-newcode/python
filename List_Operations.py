size=int(input("Size of List:"))
value=[]
total=0
for x in range(size):
    data=int(input("Enter:"))
    value.append(data)
    total+=data

reOrder=[]
for x in range(1,size+1):
    reOrder.append(value[-x])
    
print("Given List:",value)
print("Maximum:",max(value))
print("Minimum:",min(value))
print("Sum:",total)
print("Reverse:",reOrder)
