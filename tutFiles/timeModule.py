import time as t
print(t.time())
initial = t.time()
k = 0
while k < 10:
    print(k, end=" ")
    t.sleep(2)
    k += 1
print()
print(t.time()-initial)
initial2 = t.time()
for i in range(10):
    print(i, end=" ")
    t.sleep(2)
print()
print(t.time()-initial2)
print(t.asctime(t.localtime(t.time())))
