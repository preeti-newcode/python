import numpy as n

matrix=n.random.randint(1,100,(4,5))
print(matrix)

print("Row wise Sum\n")

print(sum(matrix))
print("\nOR\n")
print(matrix.sum(axis=0))
