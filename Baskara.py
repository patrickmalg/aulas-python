#ALUNO: Patrick Moreira de Albuquerque Lins Gomez
#RA: 121127

import math

def baskara(a,b,c):
    delta = (b ** 2) - (4 * a * c)
    baskara = ((-b + math.sqrt(delta)) / (2 * a))
    return baskara

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = (b ** 2) - (4 * a * c)

if delta<0:
    print('\nesta equação não possui raízes reais')

elif delta==0:
    x = baskara(a,b,c)
    print('\na raiz desta equação é', x)

elif delta>0:
    x = baskara(a,b,c)
    y = ((-b - math.sqrt(delta)) / (2 * a))
    if x <= y:
        print('\nas raízes da equação são', x, 'e', y)
    else:
        print('\nas raízes da equação são', y, 'e', x)