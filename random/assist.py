# calculator to assist with  project #1

import numpy as np
import matplotlib.pyplot as plt

vo = (55*5/18)
d = 0.8
a = -3.0
tb = (-vo/a+d)
tvalues=[(7.1)*x/71 for x in range(71)]
xfsvalues=[]
def test(x):
    for i in range(len(tvalues)):
        xfs = x + (vo * tvalues[i]) + (a*(tvalues[i])*(tvalues[i])/2)
        xfsvalues.append(xfs)
    plt.plot(tvalues,xfsvalues)
    plt.ylabel('Position (m)')
    plt.xlabel('Time (s)')
    plt.show()

test(-38)
