import numpy as np

a = np.array([1, 2, 3, 4])

# copy()
b = a.copy()
b[0] = 1111
print(a, b)


# view()
b = a.view()
b[0] = 1111  # will also reflect in a
print(a, b)
