import numpy

D1=[1,2,3]
D2=[[1,2,3],[3,4,6]]
D3=[[[1,2,3,4],[3,4,5,4]],[[1,2,6,4],[3,4,7,4]]]

arr1=numpy.array(D1)
arr2=numpy.array(D2)
arr3=numpy.array(D3)

while True:
    n=int(input("1)Dimension of array\n2)Shape of array\n3)Number of element\n:"))
    di=int(input("Choose one:\n1)One Dimension\t2)Two Dimension\t3)Multi Dimension\n:"))
    
    if di==1:
        di=arr1
    elif di==2:
        di=arr2
    else:
        di=arr3
    
    print(f"Your chosen Array \n{di}\n")
    
    if n==1:
        print("Dimension",di.ndim)
    elif n==2:
        print("Shape",di.shape)
    else:
        print("Size",di.size)
    
    repeat=input("Do you want to continue (yes/no):").upper()
    if repeat=='NO':
        break;
