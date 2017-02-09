# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt


a = np.pi/2
avalues=[np.pi/2]
x = np.pi/2
for n in range(2,31):
    a = a*((-(x**2))/(((2*n)-1)*((2*n)-2)))
    avalues.append(a)


sumN = sum(avalues)
print(sumN)
print(np.sin(x))
