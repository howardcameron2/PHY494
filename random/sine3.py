# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt

x = np.pi/4
eps=1e-16
a = np.pi/4
n=1
sumN=np.pi/4
sumvalues=[np.pi/4]
while np.abs(a/sumN) >= (1e-16):
    n=n+1
    a = a*((-((np.pi/2)**2))/(((2*n)-1)*((2*n)-2)))
    sumN+=a
    sumvalues.append(a)

print(sumvalues)
print(sumN)
print(np.sin(x))
