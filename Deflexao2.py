from Const import *

# Variáveis são iniciadas no arquivo 'Const.py'


for m in range (1,lim,2):
    for n in range (1,lim,2):

        print(f'\n\nIteração: m = {m}, n = {n}')
        # Cálculo de W_max
        sD += (np.sin(m*pi*Xd/a)*np.sin(n*pi*Yd/b))/(m*n*(((m/a)**2+(n/b)**2)**2)+(N/D)*(m/pi*a)**2)
        WMAXD = (16 * p0 / (pi ** 6 * D)) * sD
        # Contagem de iterações
        k += 1

        if(k>=2):
            er = abs((WMAXD - cache_wmaxD) / cache_wmaxD * 100)
            print(f'Erro (relativo à anterior, Deflexão2)= {er}%')

        cache_wmaxD = WMAXD

        if(er<lim_er):
            m5 = m; n5 = n
            break
    if (er < lim_er):
        m5 = m; n5 = n
        break
    m5 = m
    n5 = n

# Reiniciando variáveis auxiliares
sD = 0;WMAXD = 0;cache_wmaxD = 0


for m in range (1,m5+1,2):
    for n in range (1,n5+1,2):

        # Cálculo de W_max para o exemplo 9.1
        sD += (np.sin(m*pi*Xh/a)*np.sin(n*pi*Yh/b))/(m*n*(((m/a)**2+(n/b)**2)**2)+(N/D)*(m/pi*a)**2)
        WMAXD = 16 * p0 / (pi ** 6 * D) * sD

    cache_wmaxD = WMAXD

WplotD = cache_wmaxD                                                                      # Última iteração de Wp
k = 0                                                                                     # Contagem de iterações
