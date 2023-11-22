import numpy as np
from calcula_rigidez_flexao import calcula_rigidez_flexao

#Modulos:
import constantes

def calcula_deflexao_5p2(x,y):
    
    p0 = constantes.po
    b = constantes.lado_b
    a = constantes.lado_a
    D = calcula_rigidez_flexao()
    
    return p0 / (((np.pi ** 4) * D)) * (((1 / (a ** 2)) + (1 / (b ** 4))) ** 2) * np.sin((np.pi * x) / a) * np.sin((np.pi * y) / b)
    
    # return resultado
    

