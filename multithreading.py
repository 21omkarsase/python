import time # import time module  
import threading  

def cal_sqre(num): # define a square calculating function  
    print(" Calculate the square root of the given number")  
    for n in num: # Use for loop   
        time.sleep(0.3) # at each iteration it waits for 0.3 time  
        print(' Square is : ', n * n)  
  
def cal_cube(num): # define a cube calculating function  
    print(" Calculate the cube of  the given number")  
    for n in num: # for loop  
        time.sleep(0.3) # at each iteration it waits for 0.3 time  
        print(" Cube is : ", n * n *n)  
  
ar = [4, 5, 6, 7, 2] # given array  
  
t = time.time() # get total time to execute the functions  
th1 = threading.Thread(target=cal_sqre, args=(ar, ))  
th2 = threading.Thread(target=cal_cube, args=(ar, ))  
print('1111')
th1.start()  
print('2222')
th2.start()  
print('3333')
th1.join()  
print('44444')
th2.join()  
print('5555')
# cal_sqre(ar)
# cal_cube(ar)
print(" Total time taking by threads is :", time.time() - t) # print the total time  
print(" Again executing the main thread")  
print(" Thread 1 and Thread 2 have finished their execution.")  