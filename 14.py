# write a numpy program to create a 4x4 array with random values. Create a new array from the said array, by swapping 1st and last rows

import numpy as np

matrix = np.random.randint(1, 10, size=(4, 4))
print("original matrix")
print(matrix)

new_array = matrix.copy()

temp = new_array[0].copy()
new_array[0] = new_array[3]
new_array[3] = temp

print("after swapping")
print(new_array)
