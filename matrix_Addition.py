#matrix Addition
l=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[1,2,3],[4,5,6],[7,8,9]]
result=list()
for x in range(len(l)):
    row=[]
    for y in range(len(l[x])):
        row.append(l[x][y]+l2[x][y])
    result.append(row)
print(result)
    
