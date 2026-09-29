# write a numpy to save a given array to a text file and load it

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

np.savetxt("demo.txt", arr, "%d")
loaded_array = np.loadtxt("demo.txt", int)
print(loaded_array)
