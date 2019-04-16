nome = str(input("Nome do aluno: "))
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print("A Média do aluno {} é {:.1f}".format(nome, media))
if media <= 5.0:
    print("Situação: REPROVADO.")
elif media > 5.0 <= 6.9:
    print("Situação: em RECUPERAÇÃO.")
elif media >= 7.0:
    print("Situação: APROVADO.")