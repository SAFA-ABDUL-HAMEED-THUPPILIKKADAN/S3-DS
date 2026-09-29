# write a prgrm to create a 2D array using numpy

import numpy as np


a = np.array([[11, 32, 34], [42, 52, 63], [17, 18, 9]])
print(a)


# create a 3x3 matrix1
b = np.array([[11, 2, 13], [42, 53, 6], [72, 18, 9]])
print(b)
print(a+b)
print(a-b)
print(a*b)
c = np.dot(a, b)
print(c)

transpose_a = a.transpose()
transpose_b = b.transpose()

print(transpose_a)
print(transpose_b)

# find the determinant of a matrix a

determinant_a = np.linalg.det(a)
print(determinant_a)

# inverse of a matrix

inverse = np.linalg.inv(a)


print(inverse)

# find max and min value of a matrix

max = a.max()
min = a.min()
print(max)
print(min)

# trace values of a matrix

print(np.trace(a))


