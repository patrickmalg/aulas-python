print("-" * 70)
print("AUTO ESCOLA SP")
print("Preencha os dados a baixo para saber se está apto a dirigir.")
print("-" * 70)
nome = str(input("Digite seu nome completo: "))
nasc = int(input("Digite o ano em que você nasceu: "))
estado = str(input("Em qual estado você mora? "))
idade = 2019 - nasc
print("       ")
print("=" * 24)
print("FICHA DO USUÁRIO")
print("=" * 24)
print("Nome: {}\nIdade: {}\nEstado onde reside: {}".format(nome, idade, estado))
print("=" * 24)
print("     ")
if idade >= 18:
    print("Olá {}, você está apto para realizar o teste de direção!".format(nome))
else:
    print("Olá {}, por você ter {} anos, não será possivel realizar o teste de direção.".format(nome, idade))

