#Escreva um método que aceite um valor
#inteiro (x) como parâmetro e calcule a
#expressão:
#y = x² − 8x + 5

x = float(input("Bom dia!! informe um valor para x na expressão y = x² − 8x + 5: "))
y = x ** 2 - 8* x + 5
print("O resultado da expressão utilizando o {} em x é igual a {:.2f}".format(x, y))
