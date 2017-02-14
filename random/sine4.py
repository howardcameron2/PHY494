# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt

def sin_series(x):
    eps=1e-16
    a = x
    n=1
    sumN=x
    sumvalues=[x]
    while np.abs(a/sumN) >= (1e-16):
        n=n+1
        a = a*((-(x**2))/(((2*n)-1)*((2*n)-2)))
        sumN+=a
        sumvalues.append(a)
    print(sumN)

for i in range(20):
    sin_series(-1+i/10)
