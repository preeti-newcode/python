import numpy as n

# Create a 3D NumPy array with mixed data types
arr=n.array([[[1,2,3],[4,5,6]],[['1b','2b','3b'],['4b','5b','6b']]])

# Iterate over the 3D array and print each element
for a in arr:
    for b in a:
        for c in b:
            print("Element : ",c)
