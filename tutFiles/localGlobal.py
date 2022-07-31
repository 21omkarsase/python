# x = 20


# def localGlobal():
#     x = 30
#     print(x, "1")

#     def globaLocal():
#         global x
#         x = 40
#         print(x, "3")
#     print(x, "2")
#     globaLocal()
#     print(x, "4")


# localGlobal()
# print(x, "5")

from ast import Pass


y = 1
for i in range(5):
    print(i)
    y = y*(i+1)
print(y)


def fac(x):
    if x == 1:
        return 1
    return x*fac(x-1)


print(fac(5))
l = [1, 2, 3, 4, 5]
for i in l:
    print(i, end=" ")
print()
print("lajsdfl")
