import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])

print(a[-1])
print(a[:-1])

print(a[::-1])
print(a[2:6:2])


# 2d
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a[0][1], a[0, 1])  # both will work same
print(a[0][1:])
print(a[0][::-1])  # 3 2 1
print(a[1:])  # [[4,5,6][7,8,9]]
print("********")
print(a[1:][0])  # 4 5 6
print(a[1:][1])  # 7 8 9

for i in range(len(a)):
    a[i] = a[i][::-1]
print(a)


# 3d
a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a[0, 0, 1])  # 2
print(a[0, 0, 2:])  # 3,4

print(a[0, 1:])
print(a, a.ndim)

print(a[0, 1, 1:])
print(a[1, 0, 0:])
print(a[1, 0:])
