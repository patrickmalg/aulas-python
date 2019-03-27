#[Exercício Clássico] Faça um programa de
#conversão de temperatura de Fahrenheit (F)
#para graus Celsius (C).


print("BOM DIA!!")
print('-' * 24)
c = float(input("Informe a temperatura em °C: "))
f = (9 * c / 5) + 32
print('A temperatura de {}°C corresponde a {:.1f}°F!'.format(c, f))