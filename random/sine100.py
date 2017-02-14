# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt

def sin_series(x):
    eps=1e-16
    xvalues = [x, x*2/3, x/3]
    n=1
    sumN=x
    sumvalues=[x]
    for j in range(len(xvalues)):
        a = xvalues[j]
        while np.abs(xvalues[j]/sumN) >= (1e-16):
            n=n+1
            a = a*((-(x**2))/(((2*n)-1)*((2*n)-2)))
            sumN+=a
            sumvalues.append(a)
        print(sumN)

sin_series(5)   
