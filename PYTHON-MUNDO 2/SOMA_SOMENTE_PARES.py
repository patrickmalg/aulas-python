soma = 0
cont = 0
for num in range(1, 7):
    valores = int(input("Digite o {}° valor: ".format(num)))
    if valores % 2 == 0:
        cont = cont + 1
        soma = soma + valores
print("Você informou {} valores pares e a soma deles é {}.".format(cont, soma))
