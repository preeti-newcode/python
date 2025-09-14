import numpy as n 

matrix=n.random.randint(1,100,(4,5))

avg=matrix.mean(axis=1)

print("2D Array",matrix)
print("Average Row-wise",avg)
print(f"Maximum Value out of all avg : {max(avg)}")
