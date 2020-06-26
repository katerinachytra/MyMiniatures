import numpy as np

def sphere(img, n):
    dose = []
    R = np.mean(img.shape) / 2   
    z_d, y_d, x_d = img.shape[0], img.shape[1], img.shape[2]
    Coordin = np.meshgrid(np.linspace(-z_d + 1, z_d - 1, z_d), np.linspace(-y_d + 1, y_d - 1, y_d),
                          np.linspace(-x_d + 1, x_d - 1, x_d))
   
    Cz, Cy, Cx = Coordin[0], Coordin[1], Coordin[2]

    for z in range(z_d):
        for y in range(y_d):
            for x in range(x_d):
                if Cz[y, z, x] ** 2 + Cy[y, z, x] ** 2 + Cx[y, z, x] ** 2 <= R ** 2:
                    dose.append(img[z, y, x])
                    img[z, y, x] = n
    return dose, img
