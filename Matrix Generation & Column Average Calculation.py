import numpy as n

matrix=n.random.randint(1,100,(4,5))
print(matrix)

print(f"Average of 2nd column: {matrix[:,1].mean()}")
