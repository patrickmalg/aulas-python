preco = float(input("Qual o preço do produto? R$"))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% passou a custar R${}'.format(preco, novo))