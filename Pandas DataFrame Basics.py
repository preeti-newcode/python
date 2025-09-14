import pandas as p 
dic={'key':[40,90,100],'value':[1.5,5.1,1.1]}
df=p.DataFrame(dic)

print("DataFrame\n",df)
print()
print("Row Values\n",df.values[0])
print("Column values\n",df['key'])
print("Singles Row form a column\n",df['value'].values[1:3])
