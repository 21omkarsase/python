# addition = lambda x, y: x + y

getSquare = lambda x : x * x
print(getSquare(5))


# with map
nums = [1, 2, 3, 4]

squared_numbers = list(map(getSquare, nums))
print(squared_numbers)

# with reduce
from functools import reduce

sum = reduce(lambda a, b : a + b, nums)
print(sum)

# with filter
even_nums = list(filter(lambda x : x % 2 == 0, nums))
print(even_nums)

# sortint tuple list
nums = [(3, 2), (3, 1), (4,0)]

nums_sorted = sorted(nums, key = lambda x : x[1])
print(nums_sorted)

# conditional logic

isEven = lambda x : 1 if x % 2 == 0 else 0
print(isEven(1))
print(isEven(2))

# pssing lambda fun as argument

def perform_operation(a, b, operation):
    return operation(a, b)

print(perform_operation(3, 5, lambda a, b : a + b))
