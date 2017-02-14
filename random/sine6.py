# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt

def sin_series(x):
    eps=1e-16
    n=1
    sumN=x
    sumNvalues = []
    xvalues = [-x+(i/10) for i in range(20*x)]
    for j in range(len(xvalues)):
        while np.abs(xvalues[j]/sumN) >= (eps):
            n=n+1
            a = (xvalues[j])*((-(x**2))/(((2*n)-1)*((2*n)-2)))
            sumN+=a
        print(sumN)
        sumNvalues.append(sumN)
    print(sumNvalues)

sin_series(1)
