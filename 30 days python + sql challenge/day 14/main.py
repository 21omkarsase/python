import My_Package as P

from My_Package.Sub_Package.Child_Package.advance_math import add

sum = add(3, 5)
print("sum : ", sum)

sum = P.Sub_Package.Child_Package.advance_math.add(3, 5)
print("sum : ", sum)