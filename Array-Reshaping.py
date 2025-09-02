import numpy as n

print("1D")
ar = n.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(ar, ar.shape, sep="\n\n")

print("\n\n2D")
ar.shape = (3, 4)
print(ar, ar.shape, sep="\n\n")

print("\n\n3D")
ar.shape = (3,2,2)
print(ar, ar.shape, sep="\n\n")
