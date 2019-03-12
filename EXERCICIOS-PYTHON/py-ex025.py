nome = str(input("Digite o seu nome: ")).strip()
if nome == "Patrick":
    print("QUE BELO NOME SEU GATÃO")
else:
    print("Seu nome é uma BOSTA")
print("Bom dia, {}".format(nome))

print('=' * 30)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print("A média do aluno é {:.1f}".format(media))
if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")