class A:
    def met(self):
        print("this is method of class A")


class B(A):
    def met(self):
        print("this is method of class B")


class C(A):
    def met(self):
        print("this is method of class C")


class D(B, C):
    def met(self):
        print("this is method of class D")


a = A()
b = B()
c = C()
d = D()

d.met()
