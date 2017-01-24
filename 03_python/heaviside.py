# Heaviside step function
def heaviside(x):

    theta = None
    if x < 0:
        theta = 0.
    elif x == 0:
        theta = 0.5
    else:
        theta = 1.
    return theta

xvalues = []
thetavalues = []
for i in range(-16,17):
    x=i/4
    xvalues.append(x)
    theta = heaviside(x)
    thetavalues.append(theta)
    print("Theta(" + str(x) + ") = " + str(theta))

print(xvalues,thetavalues)

import matplotlib.pyplot as plt
plt.plot(xvalues, thetavalues, '-o', color="red", linewidth=2)
plt.show()
