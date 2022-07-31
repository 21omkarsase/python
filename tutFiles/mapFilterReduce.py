from functools import reduce


numbers = ["3", "23", "7", "7"]

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
numbers = list(map(int, numbers))

numbers[2] = numbers[0]+1
print(numbers[2])


def sq(a):
    return a*a


num = [3, 4, 6, 5, 44, 23, 77, 2]
square = list(map(lambda x: x*x, num))
print(square)


def squarE(x):
    return x*x


def cubE(x):
    return x*x*x


funct = [squarE, cubE]
for i in range(10):
    val = list(map(lambda x: x(i), funct))
    print(val)

# filter


def is_greater(x):
    return x > 5


sol = list(filter(is_greater, num))
print(sol)

# reduce
kn = reduce(lambda x, y: x+y, sol)
print(kn)
