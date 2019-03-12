nome = str(input("Nome do proprietario do veiculo: "))
marca = str(input("Marca do veiculo: "))
ano = int(input("Ano do veiculo: "))
print('=' * 24)
print("FiCHA DO VEÍCULO")
print("""O proprietario do veiculo {}, chama-se {} e comprou o carro no ano {}.
É necessario a revisão caso o veiculo tenha mais de cinco anos de uso.""".format(marca,nome,ano))
print('-' * 24)
revisao = 2019 - ano
print("O seu carro tem {} anos de uso, logo...".format(revisao))
print('=' * 24)
if revisao >= 5:
    print("É necessario fazer a revião.")
else: 
    print("Não é necessario a revisão.")
print("Obrigado!")
