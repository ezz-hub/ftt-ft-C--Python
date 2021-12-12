import ctypes
from numpy.ctypeslib import ndpointer
import matplotlib.pylab as plt
from time import time
import numpy as np
import math
x = ctypes.CDLL('./partB.so')
DFT = x.dft
FFT = x.fft
#what functions return, in case of void is none.
DFT.restype = None
DFT.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ctypes.c_double]
FFT.restype = None
FFT.argtypes =[ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),ctypes.c_int]

def test_signal(sampling_freq):

    Ts = 1/sampling_freq
    t = np.arange(0,10+Ts,Ts) #(start,stop,step)
    x = 1*np.cos(2*np.pi*3*t)+1*np.cos(2*np.pi*2000*t)+1*np.cos(2*np.pi*1000*t)+1*np.cos(2*np.pi*500*t)+1*np.cos(2*np.pi*1*t)
    y = 0*np.sin(2*np.pi*3*t)
    z = np.column_stack((x, y))
    z2 = np.column_stack((x, y))
    t_signal=[z,z2]
    return t_signal


signal_length=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]

Time=[]
Time2=[]
error = []

for N in (signal_length):
    X=test_signal(N)
    start=time()*1000
    DFT(X[0], X[1], N)
    end=time()*1000
    Time.append(end-start)

    start2=time()*1000
    FFT(X[0], N)
    end2=time()*1000
    Time2.append(end2-start2)

    MSE = np.square(np.subtract(X[0],X[1])).mean()
    RMSE = math.sqrt(MSE)
    error.append(RMSE)

print(error)
plt.plot(signal_length,Time)
plt.show()
plt.plot(signal_length,Time2)
plt.show()
plt.plot(signal_length,error)
plt.show()






