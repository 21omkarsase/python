import sys

# Every iterator is iterable
# But every iterable is not iterator

# Iterator -->
    # an iterable is an object that can be iterated upon,
    # meaning that you can traverse through all the values

nums = [num for num in range(8)]

for num in nums:
    print(num, end = " ")

print("\t")
print(nums, type(nums), sys.getsizeof(nums))

# Iterator -->
     # is an object that produces the next value in a sequence when you call next() on it.

num_iter = iter(nums)
print(num_iter, type(num_iter), sys.getsizeof(num_iter))

print(next(num_iter), end = " ") # 1
print(next(num_iter), end = " ") # 2
print(next(num_iter), end = " ") # 3
print(next(num_iter)) # 4

for it in num_iter:
    print(it, end = " ") # (5, 6, 7)

print("\t")


# checking is a iterator or iterable
# using dir function

# 1. dir(nums) -> will have __iter__ element
print('__iter__' in dir(nums)) # True
print('__iter__' in dir(4)) # False

# 2. dir(num_iter) -> will have __iter__ & __next__ element
print('__iter__' and '__next__' in dir(num_iter)) # True
print('__iter__' and '__next__' in dir(nums)) # False

print(id(num_iter))             # 2290673879936
print(id(iter(num_iter)))       # 2290673879936
