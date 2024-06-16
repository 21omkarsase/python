# Generator ->

# Generator is a special function that return a iterator

# Every Generator is a iterator
# But every iterator is not a generator

# In Python, a generator is a special type of function that
# returns an iterator object using the yield keyword

def counter(n):
    it = 0

    while it <= n:
        yield it
        it += 1

cnt = counter(5)

print(next(cnt))
print(next(cnt))

for c in cnt:
    print(c, end = " ")
print("\t")

squares = (num * num for num in range(10))
print(squares, type(squares))

print(next(squares))
print(next(squares))

for square in squares:
    print(square, end = " ")
print("\t")


# Chaining Generators

def fib_nums(nums):
    x, y = 0, 1

    for _ in range(nums):
        x, y = y, x + y

        yield x

def square(nums):
    for num in nums:
        yield num ** 2

fib_gen = fib_nums(10)
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))

print(type(fib_gen))

square_gen = square(fib_gen)
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

print(type(square(fib_nums(10))))
