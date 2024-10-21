# from multipledispatch import dispatch

# class A:
#     @dispatch(int, int)
#     def abd(self, a, b):
#         return a + b

# class B(A):
#     @dispatch(int, int, int)
#     def abd(self, a, b, c):
#         return a + b + c
#     pass

# a = A()
# b = B()

# print(a.abd(3, 2))
# print(b.abd(5, 4, 3))
# print(b.abd(5, 3))


with open('temp.txt', 'a') as file:
    def fun1(a, bc):
        a = a + bc        
        return a
        
    file.write(str(fun1) + '\n')
    
    