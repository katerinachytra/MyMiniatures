import numpy as np

def circle(R, size):
    Coordin = np.meshgrid(np.linspace(-size,size,size+1), np.linspace(-size,size,size+1))
    Cx, Cy = Coordin[0], Coordin[1]
    O = np.ones((size, size))

    for i in range(size):
        for j in range(size):
            if Cx[i][j] ** 2 + Cy[i][j] ** 2 <= R ** 2:
                O[i][j] = 0
    return O

O = circle(45, 256)
import matplotlib.pyplot as plt
plt.imshow(O, cmap="gray")
plt.show()