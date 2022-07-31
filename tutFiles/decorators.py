def func1():
    print("learn python")


func2 = func1
del func1
func2()


def funCret(num):
    if num == 0:
        return print("lkajsdf")
    elif num == 1:
        return sum([4, 5])


a = funCret(0)
print(a)


def executor(func):
    func("this")


executor(print)


def nowExec(func):
    print("executing now")
    func()
    print("Executed")


def dec(func):
    def nowExec():
        print("executing now")
        func()
        print("Executed")
    return nowExec


@dec
def func():
    print("learn py in one video")


# a = dec(func)
# func = dec(func)
func()
