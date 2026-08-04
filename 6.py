import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)

print(arr.shape)

a1 = arr.reshape(2,3)

print(a1)

print(a1.shape)

a2 = np.array([10,20,30,40])
print(a2)
print(a2.shape)

a3 = a2.reshape(4,1)
print(a3)
print(a3.shape)

a4 = arr.reshape(1,-1)
print(a4)

#arr.reshape(1,-1) , the parameter 1 make the array has one row, -1 numpy automatically calculates the number of columns

arr1 = np.array([10,20,30,40,50,60])
print(arr1)
print(arr1.shape)

a5 = arr1.reshape(1,-1)
print(a5)
print(a5.shape)
