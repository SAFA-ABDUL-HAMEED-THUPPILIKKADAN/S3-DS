# create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15

import numpy as np

arr = np.arange(0, 21)
# arr[9:16] = -arr[9:16]


for i in range(len(arr)):
    if i >= 9 and i <= 15:
        arr[i] = -1 * arr[i]

print(arr)
