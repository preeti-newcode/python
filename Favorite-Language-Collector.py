d={}
for x in range(4):
    name,lan=input("Enter Name and favorite language\n").split()
    d.update({name:lan})
    
print(d)
