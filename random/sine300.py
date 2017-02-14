# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt

x = [np.pi/2,np.pi/4]
sumNvalues = []
for j in range(len(x)):
    eps=1e-16
    a = x[j]
    n=1
    sumN=x[j]
    while np.abs(a/sumN) >= (1e-16):
        n=n+1
        a = a*((-((np.pi/2)**2))/(((2*n)-1)*((2*n)-2)))
        sumN+=a
    sumNvalues.append(sumN)
    
print(sumNvalues)
print(np.sin(x[0]),np.sin(x[1]))
