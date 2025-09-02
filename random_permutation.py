import numpy

# Create a NumPy array
arr=numpy.array([10,20,30,40,50])

# Generate a random permutation of the array
k=numpy.random.permutation(arr)

print("Original data after permutation",arr)
print("Permutated variable",k)

#The .base attribute is used to check if k is a view of the original array arr. Since np.random.permutation() returns a new array, k.base will be None.
print("\n",k.base)
