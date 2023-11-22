from sympy import diff

def calcula_derivadas(w, x, y, D, v):
    #Calcula as derivadas da função w e retorna os momentos e as tensões cortantes

    # Derivadas da função w
    dwdx = diff(w, x)
    d2wdx2 = diff(dwdx, x)

    dwdy = diff(w, y)
    d2wdy2 = diff(dwdy, y)

    d2wdxdy = diff(dwdx, y)

    # Momentos
    mx = -D * (d2wdx2 + v * d2wdy2)
    my = -D * (d2wdy2 + v * d2wdx2)
    mxy = -D * (1 - v) * d2wdxdy

    # Derivadas dos momentos
    dmdx = diff(mx, x)
    dmxydy = diff(mxy, y)
    dmxydx = diff(mxy, x)
    dmdy = diff(my, y)

    # Tensões cortantes
    qx = dmdx + dmxydy
    qy = dmxydx + dmdy

    return mx, my, mxy, qx, qy