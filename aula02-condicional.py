idade = int(input("Digite a idade: "))
if idade < 16:
    print("Não pode votar.")
elif idade >= 16 and idade < 18: 
    print("Pode votar, mas não é obrigatório.")
elif idade >= 18 and idade < 70:
    print("É obrigatório votar.")
else:
    print(" Pode votar, mas não é obrigatório.")