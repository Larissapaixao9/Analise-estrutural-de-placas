import numpy as np
import constantes


def determina_w_9p1(a,b):
    
    poisson = constantes.poisson
    E = constantes.E_aco
    c = 0.2
    d = 0.2
    p0 = 8
    P = p0/(4*c*d)
    t = 0.01
    D = (E*t**2)/(12*(1-poisson**2))
    m=2
    n=2
    y = b/2
    x = a/2

    a = np.linspace(0, 8, 100)  # Intervalo para a
    b = np.linspace(0, 16, 100)  # Intervalo para b

    a, b = np.meshgrid(a, b)

    # Calcular os valores de w
    w = ((4*P)/(np.pi**4 * D*a*b)) * ((-1)**(((m+n)/2)-1)) * ((np.sin(m*np.pi*x/a) * np.sin(n*np.pi*y/b))/(((m/a)**2 + (n/b)**2))**2)

    return a,b,w