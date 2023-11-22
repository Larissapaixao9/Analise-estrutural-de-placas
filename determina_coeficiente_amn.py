import numpy as np

def determina_coeficiente_amn():
    
    N = 10.0
    a = 6.0
    D = 4.0
    p0 = 2.0
    b = 8.0
    m = np.arange(0, 20, 1)
    n = np.arange(0, 20, 1)
    m, n = np.meshgrid(m, n)
    amn = (16*p0) / (np.pi**6 * D * m * n * ((((m**2)/(a**2)) + ((n**2)/(b**2))) + (N/D) * ((m/(np.pi*a))**2)))

    return amn,m,n




