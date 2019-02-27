print("METODO 1")
print("          ")
ca = float(input("Comprimento do cateto oposto: "))
co = float(input("Comprimento do cateto adjacente: "))
hi = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))


print('=' * 48)
print('=' * 48)


print("METODO 2")
print("          ")
import math
cat = float(input("Comprimento do cateto oposto: "))
cot = float(input("Comprimento do cateto adjacente: "))
hip = math.hypot(cat, cot)
print('A hipotenusa vai medir {:.2f}'.format(hip))




