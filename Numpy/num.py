import numpy as np 

x = np.array([1, 2, 3, 4])
print(x)
print(type(x))

# 

y = [1, 2, 3, 4]
print(y)
print(type(y))

#
import numpy as np

# 1D Array
arr = np.array([1, 2, 3, 4, 5])
print(arr)          # [1 2 3 4 5]
print(type(arr))    # <class 'numpy.ndarray'>

# 2D Array (Matrix)
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 3D Array
arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr3d)
