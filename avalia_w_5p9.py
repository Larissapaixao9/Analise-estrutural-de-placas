import numpy as np
import constantes
from calcula_rigidez_flexao import calcula_rigidez_flexao

def avalia_w_5p9():
    D = calcula_rigidez_flexao()
    P = constantes.po
    m = 0.3
    n = 0.3
    a = np.linspace(0, 5, 100)  # Intervalo para a
    b = np.linspace(0, 10, 100)  # Intervalo para b
    a, b = np.meshgrid(a, b)
    
    return ((4 * P) / (np.pi**4 * D * a * b)) * (((np.sin(m * np.pi * a) * np.sin(n * np.pi * b)) / (((m / a)**2 + (n / b)**2))**2)) * np.sin(m * np.pi * a) * np.sin(n * np.pi * b), a,b
    
