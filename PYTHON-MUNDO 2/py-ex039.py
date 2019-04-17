from datetime import date
print("=-=-=-=" * 5)
print("Confederação Nacional de Natação")
print("=-=-=-=" * 5)
nome = str(input("Nome do atleta: "))
nasc = int(input("Ano de nascimento do atleta: "))
atual = date.today().year
idade = atual - nasc
print("------" * 10)
print("O atleta {} tem {} anos de idade.".format(nome, idade))
if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 25:
    print("Categoria: SÊNIOR")
else: 
    print("Categoria: MASTER")
