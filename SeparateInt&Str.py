a=[1,'hello',2,'oops',90]
l=[]
s=[]
size=len(a)
for i in range(size):
    if type(a[i])==int:
        l.append(a[i])
    else:
        s.append(a[i])
print(a,l,s,sep='\n')
