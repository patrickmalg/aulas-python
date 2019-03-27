#Escreva um programa que, dada a idade do usuário em anos, meses e dias (admita
#valores inteiros), calcule sua idade em dias. Considere que cada ano tem 365 dias e cada
#mês 30 dias.

nome = str(input("Olá, como você se chama? "))
idadeAnos = int(input("Idade em anos: "))
idadeMeses = int(input("Em que mês você nasceu? (utilize números): "))
calc = (idadeAnos * 365) + (idadeMeses * 30)
print("{}, você viveu exatamente {} dias.".format(nome, calc))

 
