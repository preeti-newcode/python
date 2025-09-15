import pandas as pd 
import numpy as np 

l=np.random.randint(0,100,50)
l.shape=(10,5)
s1=pd.Series(l[:,0])
s2=pd.Series(l[:,1])
df=pd.DataFrame(data={'s1':s1,"s2":s2})
df2=pd.DataFrame(data=[s1,s2])

print(f"Series of s1\n{s1}\nand s2\n{s2}")
print(f"Dataframe with the help of series in dictionary\n{df}")
print(f"Dataframe with the help of series in list\n{df2}")

print(f"Over all list value\n{l}")
