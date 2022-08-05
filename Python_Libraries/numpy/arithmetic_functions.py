import numpy as np

arr = np.array([1, 2, 3, 4])

# # *****************max and min for 1d array*************
# print(np.min(arr))  # min
# print(np.max(arr))  # max
# print(np.argmin(arr))  # pos of min
# print(np.argmax(arr))  # pos of max

# # *****************max and min for multi dimensional array*************
# arr = [[7, 2, 9], [4, 5, 6], [2, 3, 11]]

# print(np.min(arr, axis=0))  # for min in col
# print(np.min(arr, axis=1))  # for min in row

# print(np.argmin(arr, axis=0))  # pos of min along cols
# print(np.argmin(arr, axis=1))  # pos of min along rows
# # same can be done to get max() and argmax()


# # sqrt()
# print(np.sqrt(arr).astype(int))
# print(np.sqrt(arr))


# #sin() and cos()
# arr = np.array([0, 30, 45, 60, 90])  # in radians
# print(np.sin(arr))
# print(np.cos(arr))

# # cumsum()
# print(np.cumsum(arr))

# # *********************Trigonometric functions***************
# # tan(x)
# # arccos()
# # arctan()
# # arcsin()  for cosec which is sin inverse
# arr = np.array([0, 1, 0.3, -1])
# print(np.arcsin(arr))

# # degree to radian
# print(np.radians(arr))
# print(np.deg2rad(arr))

# # radian to degree
# print(np.degrees(np.radians(arr)))
# print(np.rad2deg(np.deg2rad(arr)))

# # hypotenuse for right angled triangle
# a1 = [12, 3, 4, 6]
# a2 = [5, 4, 3, 8]
# # square(side1)+square(side2) = square(hypotenuse)
# print(np.hypot(a1, a2).astype(int))


# #***************Hyperbolic functions******************
# #tanh()
# # arcsinh()
# # arccosh()
# # arctanh()


# # ***************rounding functions******************

# arr = np.array([.5, 1.4, 1.5, 1.6, 2.4, 2.5, 2.6, 3.5, 4.5, 10.1])
# # rint()
# # 3.5  tries to become 4(to be positive)  4.5 tries to become 4(to remain +ve)
# print(np.rint(arr))

# # fix() it tires to achieve lowest value
# print(np.fix(arr))

# # floor()
# # ceil()

# # trunc()  returns array with truncating nums without decimal digits
# print(np.trunc(arr))

# # ***********Exponents and logarithms Functions –
# # ************
# # expt2 same as 2**x
# print(np.exp2([1, 2, 3, 4]))

# # log10()
# # log2()


# # *****************arithmetic functions***************
# # positive() returns +ve of every ele
# # negative() returns -ve of every ele

# # true_divide()
# arr1 = [2, 7, 2, 9, 1]
# arr2 = [-2, 3, 4, 5, 6]

# print(np.true_divide(arr1, arr2))
# print(np.divide(arr1, arr2))  # same
# print(np.divide(arr1, 5))  # arr1 each/5

# # floor_divide()  floor quotient
# print(np.floor_divide(arr1, arr2))

# # float_power
# # print(np.power(arr1, arr2))   neg powers not allowed
# print(np.float_power(arr1, arr2))
# # true -01 indicating decimal pos is before one place of its original pos i.e 0.25
# print(1/4 == 2.5000e-01)
# print(2.5000e-01+1)


# *****************special functions*******************
print(np.square([1, 2, 4, 5]))  # square of each
print(np.absolute([1, -2.3, 5]))  # absolute value
print(np.sign([1, -2.3, 5]))  # return sign in form of -1 and 1

# nan_to_num
# Replace NaN with zero and infinity with large finite numbers.
print(np.nan_to_num([1, 2, np.inf, np.nan]))
