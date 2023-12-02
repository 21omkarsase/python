operations = []

def math_operation(fun):
    def math_operation_wrapper(*args, **kwargs):
        operations.append((args, kwargs))
        result = fun(*args, **kwargs)

        return result

    return math_operation_wrapper

@math_operation
def add(a, b):
    return a + b

@math_operation
def multiply(a, b, c):
    return a * b * c

print(add(3, 4))
print(multiply(5, 6, 3))
print(operations)


