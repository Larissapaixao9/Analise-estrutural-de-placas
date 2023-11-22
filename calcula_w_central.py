import numpy as np
import constantes

def calcula_w_central():
    c = 0.1
    d = 0.1
    p0 = 4
    P = p0 / (4 * c * d)
    t = 0.01
    poisson = 0.3
    E = 200000000000
    D = (E * t ** 2) / (12 * (1 - poisson ** 2))
    m = 1   # Coloque o valor desejado para m
    n = 1   # Coloque o valor desejado para n
    a = np.linspace(0.1, 4, 100)  # Intervalo para a, alterei o início para evitar zeros
    b = np.linspace(0.1, 8, 100)  # Intervalo para b, alterei o início para evitar zeros
    x = a / 2
    y = b / 2

    # Criar uma grade de valores para a e b
    a, b = np.meshgrid(a, b)

    # Calcular os valores de w
    denominator = ((m / a) ** 2 + (n / b) ** 2) ** 2
    w = ((4 * P) / (np.pi ** 4 * D * a * b)) * ((-1) ** (((m + n) / 2) - 1)) * (
                (np.sin(m * np.pi * x / a) * np.sin(n * np.pi * y / b)) / denominator)
    
    # Evitar valores NaN substituindo valores que possam causar divisões por zero
    w[np.isnan(w)] = 0  # Substituir NaN por 0
    
    print (w)
    return w, a, b

