import pandas as pd 
a=[x for x in range(5)]
s=pd.Series(a,index=['a','b','c','d','e'])
print("List",a)
print("Series\n",s)
