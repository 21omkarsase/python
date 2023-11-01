# map (calculating powers)

nums = [1, 2, 3, 4]
powers = [2, 2, 2, 2]

# def x(a, b):
# 	return a ** b

# num_powers = list(map(x, nums, powers))
num_powers = list(map(lambda a, b : a ** b, nums, powers))

print(num_powers)

# filter (nums even and greater than 2)

result = list(filter(lambda x : x % 2 == 0 and x > 2, nums))
print(result)

# reduce (get max number)

from functools import reduce
mx = reduce(lambda a, b : a if a > b else b, num_powers)
mn = reduce(lambda a, b : a if a < b else b, num_powers)

print(mx)
print(mn)

# using all at same time
# get sum of squares of even numbers from nums

result = reduce(lambda a, b : a + b, list(map(lambda x : x * x, list(filter(lambda x : x % 2 == 0, nums)))))
print(result)