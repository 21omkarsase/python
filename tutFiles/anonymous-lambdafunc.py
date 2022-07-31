def add(a, b):
    return a+b

# add=lambda x,y:x-y  this is a lambada function


def a_first(a):
    return a[1]


a = [[50, 14], [0, 6], [84, 0]]
# a.sort(key=lambda x: x[0])  # or
a.sort(key=a_first)
print(a)
