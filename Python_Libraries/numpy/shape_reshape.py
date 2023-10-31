import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)

# multidimensional using ndmin
a = np.array([1, 2, 3, 4], ndmin=4)

print(a.shape, a)  # (1, 1, 1, 4) [[[[1 2 3 4]]]]

a = np.array([[1, 2, 3, 4], [4, 5, 6, 7]], ndmin=4)

print(a.shape, a)


# reshape
a = np.array([1, 2, 3, 4, 5, 6])
a = a.reshape(3, 2)
print(a, a.ndim, a.shape)

a = np.array([[1, 2, 3, 4, 5, 6, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9]])
a = a.reshape(3, 6)
print(a, a.ndim, a.shape)

# 3d
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

a = a.reshape(2, 3, 2)
a = a.reshape(6, 2, 1)
a = a.reshape(6, 1, 2)
print(a, a.shape, a.ndim)

a = a.reshape(12)  # onde D array with 12 cols
# or
print("abc", a)
# a=a.reshape(-1)  to convert to 1d array
a = np.reshape(a, (6, 2))
# print(a.shape[0]*a.shape[1])
print(a, a.shape, a.ndim)

# broadcasting
# print(np.add([1, 2, 3], [4, 5]))  it will lead to broadcasting err
a1 = np.array([[1, 2, 3], [1, 2, 3]])
a2 = np.array([[3], [4]])

print(a1, a2)
print(np.add(a1, a2))  # this won't give err
# we need same size arrays
# or if rows are same then for one of the array col must be 1
# or if cols are same then for one of the array row must be 1
