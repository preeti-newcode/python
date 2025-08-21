#Reverse String
value=input("Enter:")
result=list()
for x in range(len(value)-1,-1,-1):
    result.append(value[x])
result="".join(result)

print("Reverse String of",value,":",result)
