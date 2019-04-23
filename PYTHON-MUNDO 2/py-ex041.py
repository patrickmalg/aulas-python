peso = float(input("Informe o seu peso em Kg: "))
altura = float(input("Informe a sua altura em metros: "))
imc = peso / (altura ** 2)
print("===" * 5)
print("Seu IMC: {:.1f}".format(imc))
print("===" * 5)
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Parabéns! Você está com o peso ideal.")
elif 25 <= imc < 30:
    print("Sobrepeso! faça uma dieta.")
elif 30 <= imc < 40:
    print("Você está no nivel de OBESIDADE, tome cuidado!")
elif imc >= 40:
    print("OBESIDADE MÓRBIDA, procure um médico.")
