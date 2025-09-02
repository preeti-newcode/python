import numpy as n

# Create a 3D NumPy array
ar=n.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
    ])

print("Original\n",ar)

# Create a copy and view of the array
Copy=ar.copy()
View=ar.view()

# Modify the original array
ar[0,:,0]=1000

print("\nOriginal after change",ar,"Copied",Copy,"Viewed",View,sep='\n\n')
