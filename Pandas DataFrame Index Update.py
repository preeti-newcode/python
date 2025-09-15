import pandas as pd 
from numpy import random as ran
l=ran.randint(1,10,(5,6))
df=pd.DataFrame(index=['10','20','30','40','50'],data=l,columns=['a','b','c','d','e','f'])

print("Data Frame\n",df)
df.index=['i','ii','iii','iv','v']
print(f"Dataframe After index updation\n{df}")
