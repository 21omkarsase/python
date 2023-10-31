import numpy as np

arr = np.array([1, 2, 3, 4, 5, 2, 2, 3, 5, 6, 67, 72, 4])

# searching
# where
b = np.where(arr < 5)
print("abc",b, "xyz")
b = np.where(arr > 6)
print("start",b, "end")  # tuple of list of indexes to conditional ele ([1,2,3],)

a = np.arange(1,11)
print("aa", a)
# (condition,this operation will be perform on ele satisfying cond,this operation on those who won't satisfy cond)
print(np.where(a < 5, a*10, a*5))

a = np.array([[1, 2, 2, 4, 5], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])

print(np.where(a & 1, -1, 1))

print("**************serachsorted()***********")

# searchsorted()  only on sorted array
# return index at which ele will fit at its appropriate pos in array
x = np.array([1, 2, 4, 5])

y = np.searchsorted(x, 3)
print("out1",y)
y = np.searchsorted(x, 4, side="right")  # it will give from right side
print("out2",y)

print("**************insert()***********")

# insert()
a = np.array([1, 2, 3, 4, 6])
a = np.insert(a, 4, 5)
print("ar", a)
a = np.array([[10, 20, 30, 40, 50], [10, 20, 30, 40, 50]])
# np.insert(a, 0, 90) like this og array will not modify
# axis 1 will make 2d array inserting ele to 0 pos(start)
a = np.insert(a, 0, [90, 80, 80, 49, 20], axis=0)
print(a)


print("**************sort()***********")

# sort()
print(np.sort([4, 3, 2, 4, 52, 24]))
# for 2d
print(np.sort([[3, 2, 1, 5], [5, 3, 6, 2]]))
# axis 0 for col (defaut row)
print(np.sort([[3, 2, 1, 5], [5, 3, 6, 2]], axis=0))

print("**************filter()***********")

# print([1,2,3,4,5,6][i&1])
v1 = np.array([1, 2, 3, 4, 5])
v2 = [True, False, True, False, True]

l = [1, 2, 3]
a = list(filter(lambda x: x > 1, v1))
print(a)

print(v1[v2])  # will return list for true indexes
