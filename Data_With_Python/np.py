import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))


# create 2D array
mat = np.array([[1, 2, 3], [4, 5, 6]])
# print(mat)

# create 3D array
ten = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(ten)


# Check dimension
# print(arr.ndim)
# print(mat.ndim)
# print(ten.ndim)

# access element
print(arr[::2])
print(arr.dtype)
