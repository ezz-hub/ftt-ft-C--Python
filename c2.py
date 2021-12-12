import ctypes
from numpy.ctypeslib import ndpointer
from vector import Vector
import matplotlib.pylab as plt
from time import time
import numpy as np
x = ctypes.CDLL('./oRamadan.so')




# y = [1, 1, 1, 1, 1]

# x.ret.argtypes = [ctypes.c_int]
# x.ret.restype = None

# x.ret(y)

# print(type(y))
#initialize the function to be in c_types
fun = x.dft2
fun2=x.fft6
fun.restype = None
fun.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),


                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),


                ctypes.c_double]


fun2.restype = None
fun2.argtypes =[ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),ctypes.c_int]



test_sample = []
N = 16384

Ts = 1/N
t = np.arange(0,10+Ts,Ts) #(start,stop,step)
x = 1*np.cos(2*np.pi*4000*t)+1*np.cos(2*np.pi*2000*t)+1*np.cos(2*np.pi*1000*t)+1*np.cos(2*np.pi*500*t)+1*np.cos(2*np.pi*1*t)
y = 0*np.sin(2*np.pi*3*t)
z = np.column_stack((x, y))
z2 = np.column_stack((x, y))
z3=np.column_stack((x, y))
z4 = np.column_stack((x, y))
z5=np.column_stack((x, y))
z6=np.column_stack((x, y))



print(z2)

print("Helloooooooo")

test=[1,2,4,8,16,32,64,128,256,521,1024,2048,4096,8192]
test2=[1,2,4,8,16,32,64,128,256,521,1024,2048,4096,8192]
Time=[]
for i in (test):
    start=time()*1000

    fun(z, z2, i)
    end=time()*1000
    Time.append(end-start)

plt.plot(test,Time)
plt.show()


######################################
Time2=[]
for i in (test2):
    start=time()*1000
    fun2(z3, i)
    end=time()*1000
    Time2.append(end-start)

plt.plot(test2,Time2)
plt.show()

fun(z5, z4, 8192)
fun2(z6, 8192)
plt.plot(z6,z4)
plt.show()



print(z4.shape)
print(z6.shape)
