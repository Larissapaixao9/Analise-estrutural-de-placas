import numpy as np
from sympy.utilities.lambdify import lambdify
import constantes

def converte_expressoes(mx, my, mxy,qx,qy,w,x,y):
    a = constantes.a
    b = constantes.b
    mx_func = lambdify((x, y), mx, 'numpy')
    my_func = lambdify((x, y), my, 'numpy')
    mxy_func = lambdify((x, y), mxy, 'numpy')
    qx_func = lambdify((x, y), qx, 'numpy')
    qy_func = lambdify((x, y), qy, 'numpy')
    w_func = lambdify((x, y), w, 'numpy')

    # Generate a range of x and y values
    x_vals = np.linspace(0, a, 50)
    y_vals = np.linspace(0, b, 50)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Evaluate the functions at the x and y values
    Mx = mx_func(X, Y)
    My = my_func(X, Y)
    Mxy = mxy_func(X, Y)
    Qx = qx_func(X, Y)
    Qy = qy_func(X, Y)
    W = w_func(X, Y)
    
    x_vals = np.linspace(0, a, 50)
    y_vals = np.linspace(0, b, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    return Mx, My,Mxy,Qx,Qy,W,X,Y