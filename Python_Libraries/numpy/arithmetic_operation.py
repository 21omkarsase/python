import numpy as np

arr = np.array([1, 2, 3, 4])

# + , - , * , / , % , // can be performed on every ele of 1d arr at one time
print(arr*3)  # [3,6,9,12]


# for 2 1D arrays
a1 = np.array([1, 2, 3, 4])
a2 = np.array([5, 7, 8, 9])

print(a1+a2+arr)  # or
# this fun will consider only first 2 arguments to get add
print(np.add(a1, a2, a1), " addition of 3")
# i.e np.add(a1,a2)

print(a2/a1)  # or np.divide(a2,a1)       #division
# print(np.divide(a2, a1))

print(np.power(a1, a2))  # power
print(np.power(a1, a2).size)  # size of an array

# reciprocal
print(np.reciprocal(a1))

# substract
a1 = np.array([1, 2, 3, 4])
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

print(a-b-2+10)  # can do in this way
sub_ans = np.subtract(a, b, a1)  # we can't do for multiple arrays at same time

# mod or remainder
print(np.mod(a, b))
print(np.remainder(a, b))


# ***********other arithmetic operations************
# mean
print(np.mean(a1))
# average
print(np.average(a1))
# sum
print(np.sum(a1))
# variance var()
print(np.var(a1))
# 2, 7, 3, 12, 9
# mean=6.6
# v= [(mean-ele)^2] for each ele
# var=sum(v)/total ele


# ******************for Multidimensional arrays********************
a1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(np.add(a1, a2))
print(np.multiply(a1, a2))
print(np.subtract(a1, a2))
