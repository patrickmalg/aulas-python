#RA ALUNO: 121127

#Uma concessionária de veículos calcula o
#preço de venda de seus carros considerando
#um imposto total de 54% sobre o valor de
#fábrica e uma receita de 18% sobre o mesmo
#valor. Assim, dado o valor de fábrica de um
#veículo, calcule seu valor de venda.

preço = float(input("Valor de fábrica do veículo: R$"))
imposto = preço * 54 / 100
receita = preço * 18 / 100
valorVeiculo = preço + imposto + receita
print("O preço de venda do veículo é de R${:.1f}".format(valorVeiculo))
