class A:
    def met(self):
        print("this is method of class A")


class B(A):
    pass
    # def met(self):
    #     print("this is method of class B")


class C(A):
    pass
    # def met(self):
    #     print("this is method of class C")


class D(B, C):
    # def met(self):
    #     print("this is method of class D")
    pass


a = A()
b = B()
c = C()
d = D()

d.met()
