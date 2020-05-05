import numpy as np
from numpy import sqrt, pi, exp


# symmetrical 2D gaussian
def gauss2D(s,r, sigma, mu):
    y = 1/sqrt(2*pi*sigma**2)*exp(-((s-mu)**2+(r-mu)**2)/(2*sigma**2))
    return y

def circle(R, size):
    Coordin = np.meshgrid(np.linspace(-size,size,size+1), np.linspace(-size,size,size+1))
    Cx, Cy = Coordin[0], Coordin[1]
    O = np.ones((size, size))

    for i in range(size):
        for j in range(size):
            O[i][j] = gauss2D(Cx[i][j],Cy[i][j],R,0)
    return O

O = circle(64, 256)
import matplotlib.pyplot as plt
plt.imshow(O, cmap="gray")
plt.show()