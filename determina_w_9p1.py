import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from calculos_auxiliares_deslocamento import calcular_w

def determina_w_9p1():
    a = 4
    b = 4
    t = 0.01
    E = 200000
    m = 1
    n = 1
    p0 = 10
    poisson = 0.3
    D = (E * t**2) / (12 * (1 - poisson**2))
    x = np.linspace(0, a, 100)
    y = np.linspace(0, b, 100)
    X, Y = np.meshgrid(x, y)

    N_values = [1, 5000, 50000, 500000]
    for i, N in enumerate(N_values):
        Z = calcular_w(X, Y, N,p0,a,D,b)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('w')
        ax.set_title(f'N = {N}')
        plt.show()

