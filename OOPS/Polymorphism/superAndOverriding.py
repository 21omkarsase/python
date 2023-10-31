class A:
    var1 = "I am class var of A"

    def __init__(self):
        self.var1 = "I am instance var of A"


class B(A):
    var1 = "I am class var of B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am instance var of b"
        print("11",A().var1)
        print(super().var1)
        pass


a = A()
b = B()
print(b.var1)  # will not print var1 of b  it will print instance var of class a if constructor isn't called in class b
