from Const import *

# Variáveis são iniciadas no arquivo 'Const.py'

P = p0*np.sin(pi*X/a)*np.sin(pi*Y/b)

def Qxx(xis=X,yis=Y):                                                           # Qx(x,y)
    return p0/(pi*a*(1/a**2+1/b**2))*np.cos(pi*X/a)*np.sin(pi*Y/b)
def Qyy(xis=X,yis=Y):                                                           # Qy(x,y)
    return p0/(pi*b*(1/a**2+1/b**2))*np.sin(pi*X/a)*np.cos(pi*Y/b)

qtx = Qxx(X, Y)
qty = Qyy(X,Y)

