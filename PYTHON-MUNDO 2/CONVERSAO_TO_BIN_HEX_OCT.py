num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL""")
opçao = int(input("Opção: "))
if opçao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opçao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opçao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")