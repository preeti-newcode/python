import numpy as n

matrix=n.random.randint(1,100,(10,5))
print(matrix)

print(f"Average of First five rows of 3rd and 4th column:{matrix[:5,2:4].mean()}")
