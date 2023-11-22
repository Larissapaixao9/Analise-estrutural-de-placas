import numpy as np

#Importa modulos
import constantes
from calcula_rigidez_flexao import calcula_rigidez_flexao

def calcula_momento_Mx_5p2(x,y):
    D = calcula_rigidez_flexao()
    
    a = constantes.lado_a
    b = constantes.lado_b
    poisson = constantes.poisson
    p0 = constantes.po
    
    return (p0 / ((np.pi**2) * ((1 / a**2) + (1 / b**2))**2)) * ((poisson / a**2) + (1 / b**2)) * np.sin((np.pi * x) / a) * np.sin((np.pi * y) / b)
    

