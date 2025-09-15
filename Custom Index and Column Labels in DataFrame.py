import pandas as pd
from numpy import random as ran 

value=ran.randint(1,100,100)
value.shape=(10,10)
df=pd.DataFrame(value)
df.index=['R'+str(i) for i in range(1,11)]
df.columns=['C'+str(i) for i in range(1,11)]
print(df)
