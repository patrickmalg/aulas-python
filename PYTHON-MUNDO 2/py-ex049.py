sexo = str(input("Informe seu sexo [M/N]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos, por favor informe seu sexo: ")).strip().upper()[0]
print("Sexo {} registrado!".format(sexo))
