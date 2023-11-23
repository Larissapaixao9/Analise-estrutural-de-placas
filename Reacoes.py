from Const import *

def Rx(xis=X,yis=Y):
    rx = ((-p0)/(pi*a*(1/a**2+1/b**2)**2))*(1/a**2+(2-poi)/b**2)*np.sin(pi*Y/b)
    return rx

def Ry(xis=X,yis=Y):
    ry = ((-p0)/(pi*b*(1/a**2+1/b**2)**2))*((3-poi)/(b**2))*np.sin(pi*X/a)
    return ry


Rxx = Rx(X,Y)
Ryy = Ry(X,Y)

RCC =2*p0*(1-poi)/(pi**2*a*b*(1/a**2+1/b**2)**2)

# # Nas bordas, x=0, y=0
# rx = -p0 / (pi * a * (1 / a ** 2 + 1 / b ** 2) ** 2) * (1 / a ** 2 + (2 - poi) / b ** 2) * np.sin(pi * 0 / b)
# ry = -p0 / (pi * b * (1 / a ** 2 + 1 / b ** 2) ** 2) * (1 / b ** 2 + (2 - poi) / a ** 2) * np.sin(pi *0 / a)
# print(rx,ry,RCC)

