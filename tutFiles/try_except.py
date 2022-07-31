num1 = input("num 1 : ")
num2 = input("num 2 : ")

try:
    print(int(num1)+int(num2))
except Exception as e:
    print(e)
print("always print this")
