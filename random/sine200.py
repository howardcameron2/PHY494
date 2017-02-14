# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt

x = 1
#for j in range(3):
eps=1e-16
n=1
sumN=1
a = 1
sumvalues=[1]
while np.abs(a/sumN) >= (1e-16):
    n=n+1
    a = x*((-(x**2))/(((2*n)-1)*((2*n)-2)))
    sumN+=a
    sumvalues.append(a)

print(sumvalues)
print(sumN)
