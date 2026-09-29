# write a python program

# 1) to read no: of rows and cols of a matrix 1

# 2) create matrix 1

# 3) to read no: of rows and cols of a matrix 2

# 4) create matrix 2

# 5) find dot product, transpose of both matrices, trace of both

# 6) rank of both,determinant of matrix 1,inverse of matrix 2

import numpy as np

rows1 = int(input("Enter the number of rows of matrix 1:"))
cols1 = int(input("Enter the number of cols of matrix 1:"))
matrix1 = np.zeros((rows1, cols1), int)
for i in range(rows1):
    for j in range(cols1):
        matrix1[i][j] = int(input(f"Enter element matrix[{i}][{j}] : "))


rows2 = int(input("Enter the number of rows of matrix 2:"))
cols2 = int(input("Enter the number of cols of matrix 2:"))
matrix2 = np.zeros((rows2, cols2), int)
for i in range(rows2):
    for j in range(cols2):
        matrix2[i][j] = int(input(f"Enter element matrix[{i}][{j}] : "))

dot_product = np.dot(matrix1, matrix2)
t1 = matrix1.transpose()
t2 = matrix2.transpose()
tr1 = np.trace(matrix1)
tr2 = np.trace(matrix2)
det1 = np.linalg.det(matrix1)
inv2 = np.linalg.inv(matrix2)
rank1 = np.linalg.matrix_rank(matrix1)
rank2 = np.linalg.matrix_rank(matrix2)

print(dot_product)
print(t1)
print(t2)
print(tr1)
print(tr2)
print(det1)
print(inv2)
print(rank1)
print(rank2)
