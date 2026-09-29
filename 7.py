# write a numpy program to create an element wise comparison of give 2 arrays

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5])
print(a)
print(b)

print(np.greater(a, b))
print(np.greater_equal(a, b))
print(np.less(a, b))
print(np.less_equal(a, b))
print(np.equal(a, b))
print(np.not_equal(a, b))
