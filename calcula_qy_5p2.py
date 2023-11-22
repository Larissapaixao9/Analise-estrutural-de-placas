import numpy as np

import constantes

def calcula_qy_5p2(x,y):
    a = constantes.lado_a
    b = constantes.lado_b
    p0 = constantes.po
    
    return ((p0) / ((np.pi * b) * ((1 / a**2) + (1 / b**2)))) * np.sin(np.pi * x / a) * np.cos(np.pi * y / b)