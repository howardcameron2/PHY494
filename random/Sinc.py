# Sinc function

import numpy as np
import matplotlib.pyplot as plt
def sinc(x):
    if x == 0:
        return 1.0
    else:
        return np.sin(x)/x

print(sinc(0))
