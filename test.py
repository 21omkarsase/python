from multipledispatch import dispatch

class A:
    @dispatch(int, int)
    def abd(self, a, b):
        return a + b

class B(A):
    @dispatch(int, int, int)
    def abd(self, a, b, c):
        return a + b + c
    pass

a = A()
b = B()

print(a.abd(3, 2))
print(b.abd(5, 4, 3))
print(b.abd(5, 3))
