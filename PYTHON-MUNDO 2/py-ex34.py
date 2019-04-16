casa = float(input("Valor da casa? R$"))
salario = float(input("Informe o sálario do comprador R$"))
anos = int(input("Quantos anos de financiamento? ")) 
prestaçao =  casa / (anos * 12)
minimo = salario * 30 / 100
if prestaçao <= minimo:
    print("Empréstimo concedito.")
else:
    print("Empréstimo negado.")
print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(casa, anos, prestaçao))


