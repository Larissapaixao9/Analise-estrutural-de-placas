import numpy as np

import constantes

def calcula_qx_5p2(x,y):
    a = constantes.lado_a
    b = constantes.lado_b
    p0 = constantes.po
    
    return (p0 / (np.pi * a * ((1 / a**2) + (1 / b**2)))) * np.cos(np.pi * x / a) * np.sin(np.pi * y / b)