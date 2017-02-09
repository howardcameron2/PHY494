# Calculating a sine series

import numpy as np
import matplotlib.pyplot as plt

x = np.pi*0.5
a = x
avalues=[x]
for n in range(2,31):
    a = a*((-(x**2))/(((2*n)-1)*((2*n)-2)))
    avalues.append(a)


sumN = sum(avalues)
print(sumN)
print(np.sin(x))
