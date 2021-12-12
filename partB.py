import ctypes
from numpy.ctypeslib import ndpointer
import matplotlib.pylab as plt
from time import time
import numpy as np
Library = ctypes.CDLL('./RModified.so')
DFT = Library.dft
FFT=Library.fft
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
    z3=np.column_stack((x, y))
    s_freq=[z,z2,z3]
    return s_freq





print("Helloooooooo")

signal_length=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]

Time=[]
Time2=[]
error = []

for i in (signal_length):
    X=test_signal(i)
    start=time()*1000
    DFT(X[0], X[1], i)
    end=time()*1000
    Time.append(end-start)

    start2=time()*1000
    FFT(X[2], i)
    end2=time()*1000
    Time2.append(end2-start2)

    RMS = np.square(np.subtract(X[1],X[2])).mean()
    error.append(RMS)

print(error)
plt.plot(signal_length,Time)
plt.show()
plt.plot(signal_length,Time2)
plt.show()
plt.plot(signal_length,error)
plt.show()






