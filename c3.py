import ctypes
from numpy.ctypeslib import ndpointer
from vector import Vector
import matplotlib.pylab as plt
from time import time
import numpy as np
x = ctypes.CDLL('./RModified.so')
DFT = x.dft
FFT=x.fft
#what functions return, in case of void is none.
DFT.restype = None
DFT.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ctypes.c_double]
FFT.restype = None
FFT.argtypes =[ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),ctypes.c_int]



test_sample = []

def Breaker(Size):
    N = Size

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
    Zere=[z,z2,z3,z4,z5,z6]
    return Zere





print("Helloooooooo")

test=[1,2,4,8,16,32,64,128,256,521,1024,2048,4096,8192]
test2=[1,2,4,8,16,32,64,128,256,521,1024,2048,4096,8192]
Time=[]
for i in (test):
    X=Breaker(i)
    start=time()*1000

    DFT(X[0], X[1], i)
    end=time()*1000
    Time.append(end-start)

plt.plot(test,Time)
plt.show()


######################################

Time2=[]
for i in (test2):
    X=Breaker(i)
    start=time()*1000
    FFT(X[2], i)
    end=time()*1000
    Time2.append(end-start)

plt.plot(test2,Time2)
plt.show()

X = Breaker(8192)
DFT(X[4], X[3], 8192)
FFT(X[5], 8192)
plt.plot(X[5],X[3])
plt.show()



