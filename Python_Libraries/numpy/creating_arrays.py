import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr, type(arr))


# array input
l = []
for i in range(1, 5):
    ipt = int(input("Enter : "))
    l.append(ipt)

print(np.array(l))  # list to numpy array

# dimension type of array
print(arr.ndim)

# 2d array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr, arr.ndim)

# 3d array
arr = np.array([[[1, 2], [3, 4], [5, 6]], [
               [1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]])
print(arr, arr.ndim)


# multi dimensional array
arr = np.array([1, 2, 3, 4], ndmin=10)
print(arr, arr.ndim)

# ******* matrix()   #for 2d only
# string input
print(np.array([['1', '2'], ['3', '4']]))
print(np.array([[1, 2], [3, 4]]))

a = np.matrix('1 2; 3 4')
print("Via string input : \n", a, "\n\n", type(a))

# array-like input
b = np.matrix([[5, 6, 7], [4, 6]], dtype=object)
print("Via array-like input : \n", b, type(b))

# mat()
print(np.mat([[1, 2, 3, 4], [3, 4, 5, 6], [1, 2, 3, 4]]),
      np.mat([[1, 2, 3, 4], [3, 4, 5, 6], [1, 2, 3, 4]]).ndim)

# bmat()
print()

# empty array
ept = np.empty(2, dtype=int)
print(ept, type(ept), ept.ndim)

ept = np.empty([2, 2], dtype=int)
print(ept, type(ept), ept.ndim)

# zero array
zer_arr = np.zeros((3, 3, 3, 3), dtype=int)
zer_arr = np.zeros((3, 3), dtype=int)
print(zer_arr, type(zer_arr), zer_arr.ndim)

# zeros_like
arr = [1, 2, 3, 4]
arr = np.zeros_like(arr)
print(arr)

# one array
one_arr = np.ones(5, dtype=int)
print((one_arr), one_arr.ndim, type(one_arr[0]))
one_arr = np.ones((3, 3), dtype=int)
print((one_arr), one_arr.ndim, type(one_arr[0][0]))

# ones_like()
arr = np.array([[2, 3, 4, 5], [4, 3, 2, 1]])
arr_one_like = np.ones_like(arr)
print(arr_one_like)

# full like
print("*****************full like***************")
arr = np.full_like(arr, 15)
print(arr)


# arrange
print("***************arrange************")
arr = np.arange(5)
print(arr)
arr = np.arange(2, 7, dtype=int)
print(arr)


# diagonal ele=1
print("*****************only diagnoal one***********")
arr = np.eye(2, dtype=int)  # 2*2
arr = np.eye(2, 5, dtype=int)  # 2*5
print(arr, arr.ndim, type(arr))


# linespace
print("*****************linespace***********")
arr = np.linspace(10, 20, num=7, dtype=int)
arr = np.linspace(10, 20, num=5, dtype=int)
arr = np.linspace(10, 20, num=6, dtype=int)
print(arr, arr.ndim)


# **********************numpy arrays with random functions***************************
print("**********************numpy arrays with random functions***************************")
# random.ran()                     (0,1)
ran_arr = np.random.rand(7)
ran_arr = np.random.rand(2, 3)  # 2*3
print(ran_arr)

# random_randn()              closest to zero (-ve or +ve)  (less than 2 or -2)
ran_arr = np.random.randn(5)
print(ran_arr)

# random.ranf()                    [0,1)
ran_arr = np.random.ranf(5)
print(ran_arr)

# random.randint()             (min,max(exclusive),total)
ran_arr = np.random.randint(5, 7, 3)
print(ran_arr)


# ******************other methods for array creation****************
# identity()
id_arr = np.identity(3, dtype=int)
print(id_arr)
# same can be achieved by .eye()
# arr = np.eye(3, 3, dtype=int)
# print(arr)

# diag()
arr = np.array([[1, 21, 30], [63, 434, 3], [54, 54, 56]])
print(np.diag(arr))     # return array of diagonal ele
print(np.diag(arr, 1))  # returns array of next daigonal above to main diagonal
print(np.diag(arr, -1))  # returns array of next daigonal above to main diagonal
print(arr)

# diagflat()  ([diagonal ele],position)]
print(np.diagflat([1, 3, 4]))
print(np.diagflat([1, 2, 4], 1))
print(np.diagflat([1, 2, 4], -1))

# tri()     #fill all with ones except above/below specified diagnoal no(zeros)
print(np.tri(3, 3, 0, dtype=int))
print(np.tri(3, 3, 1, dtype=int))
print(np.tri(3, 3, -1, dtype=int))

# tril()  for lower triangular matrix
print(np.tril(arr))  # tril(arr,diagonal no w.r.t main diagonal(default=0))
print(np.tril(arr, -1))

# triu()  for upper triangular matrix
print(np.triu(arr))  # triu(arr,diagonal no w.r.t main diagonal(default=0))
print(np.triu(arr, 1))
