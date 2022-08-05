import numpy as np

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type(void)

arr = np.array([1, 2, 3, 4])  # int32
print("data type : ", arr.dtype)

arr = np.array([1.0, 1.2, 1.3, 1.5])  # float64
print("data type : ", arr.dtype)

# The U data type stores each Unicode character as a 32 bit integer(i.e. 4 bytes).

# <U1 unicode string type for characters
arr = np.array(['a', 'b', 'c', 'd'])
print("data type: ", arr.dtype)

# U3 unicode string type for strings where 3 is max ele len
arr = np.array(["abd", "bcc", "ccc", "dcc"])
print("data type: ", arr.dtype)

# U11 unicode string for mixed data type
arr = np.array(["d", 3, 4.3])  # nums also get converted to str in mix with str
print("data type : ", arr.dtype, type(arr[0]))


# *************data type conversion**************************
arr = np.array([1, 2, 3, 4], dtype=np.int_)
print(arr.dtype)  # int8
print(np.array(arr, dtype="f").dtype)  # float32

# int to float
arr = np.array([1, 2, 3, 4])
new_arr = np.float32(arr)
# new_arr = np.int_(arr)  #float to int32
print("data type of new_arr : ", new_arr.dtype, arr.dtype)


# astype
new_arr = arr.astype(float)  # float64
print("data types : ", arr.dtype, new_arr.dtype)


print(np.ulonglong([1.0, 2.0, 3.0]).dtype)
# Numpy type

# C type

# Description

# numpy.bool_

# bool

# Boolean(True or False) stored as a byte

# numpy.byte

# signed char

# Platform-defined

# numpy.ubyte

# unsigned char

# Platform-defined

# numpy.short

# short

# Platform-defined

# numpy.ushort

# unsigned short

# Platform-defined

# numpy.intc

# int

# Platform-defined

# numpy.uintc

# unsigned int

# Platform-defined

# numpy.int_

# long

# Platform-defined

# numpy.uint

# unsigned long

# Platform-defined

# numpy.longlong

# long long

# Platform-defined

# numpy.ulonglong

# unsigned long long

# Platform-defined

# numpy.half / numpy.float16

# Half precision float: sign bit, 5 bits exponent, 10 bits mantissa

# numpy.single

# float

# Platform-defined single precision float: typically sign bit, 8 bits exponent, 23 bits mantissa

# numpy.double

# double

# Platform-defined double precision float: typically sign bit, 11 bits exponent, 52 bits mantissa.

# numpy.longdouble

# long double

# Platform-defined extended-precision float

# numpy.csingle

# float complex

# Complex number, represented by two single-precision floats(real and imaginary components)

# numpy.cdouble

# double complex

# Complex number, represented by two double-precision floats(real and imaginary components).

# numpy.clongdouble

# long double complex

# Complex number, represented by two extended-precision floats(real and imaginary components).
