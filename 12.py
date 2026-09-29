# create a matrix and to compute sum of all elemnts, sum of each column and sum of each row

import numpy as np

# matrix = np.array([
#     [1, 2, 3], [4, 5, 6], [7, 8, 9]
# ])

# sum = np.sum(matrix)
# print(sum)

# row_sum = np.sum(matrix, axis=1)
# col_sum = np.sum(matrix, axis=0)

# print(row_sum)
# print(col_sum)


arr1 = np.arange(1, 10)

arr2 = np.reshape(arr1, (3, 3))

sum = np.sum(arr2)
row_sum = np.sum(arr2, axis=1)
col_sum = np.sum(arr2, axis=0)
print(sum)
