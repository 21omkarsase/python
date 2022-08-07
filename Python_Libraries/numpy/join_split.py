import numpy as np

# *********************JOIN*************************

a = np.array([1, 2, 3, 4, 7])
b = np.array([8, 7, 6, 5, 9])

c = np.array(
    [[1, 2, 3, 4, 7], [101, 102, 103, 104, 105], [11, 12, 13, 14, 17]])
d = np.array(
    [[8, 7, 6, 5, 9], [201, 202, 203, 204, 205], [18, 17, 16, 15, 25]])

# concatenation
print(np.concatenate((a, b)), "\n")  # 1d

print(np.concatenate((c, d), axis=1), "\n")  # 2d  1 for row
print(np.concatenate((c, d), axis=0), "\n")  # 2d  0 for col


# stack(),hstack(),vstack() & dstack() for merging

print(np.hstack((c, d)), "\n")  # same as concatenation along axis 1 (row)
print(np.vstack((c, d)), "\n")  # same as concatenation along axis 0 (col)
print(np.dstack((c, d)), "\n")  # will generate 3d array


# *********************SPLIT*************************

a = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(a, 3)  # will generate list of 3 ndarrays
new_arr = np.array(new_arr)  # converting list to array

print(type(new_arr), new_arr, "\n")

a = np.array([[1, 2], [3, 4], [6, 7], [8, 9], [
             6, 7], [8, 9], [8, 9], [6, 7], [8, 9]])

print(np.array(np.array_split(a, 3)))

# spliting along axis
print(np.array(np.array_split(a, 2, axis=0)), "\n")
print(np.array(np.array_split(a, 2, axis=0)), "\n")
print(np.array(np.array_split(a, 2, axis=1)),
      np.array(np.array_split(a, 2, axis=1)).shape, "\n")
