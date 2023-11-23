import numpy as np
m = 1
n = 1
def calcular_w(x, y, N,p0,a,D,b):
    P = ((16 * p0) / (np.pi**2)) * (1 / (m * n)) * np.sin(m * np.pi * x / a) * np.sin(n * np.pi * y / b)
    return ((16 * P) / ((np.pi**6) * D)) * (np.sin(m * np.pi * x / a) * np.sin(n * np.pi * y / b)) / (
                m * n * ((((m**2) / (a**2)) + ((n**2) / (b**2)))**2 + (N * D) * (m / (np.pi * a))**2))
