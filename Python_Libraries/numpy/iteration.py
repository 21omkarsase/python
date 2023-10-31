import numpy as np

a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [7, 8, 9]]])

for i in a:
    for j in i:
        for k in j:
            print(k, end=" ")
print()


# nditer()
for i in np.nditer(a):
    print(i, end=" x ")
print("end  1")

# ndenumerate()  will print idx and value
for idx, val in np.ndenumerate(a):
    print(idx, val)
