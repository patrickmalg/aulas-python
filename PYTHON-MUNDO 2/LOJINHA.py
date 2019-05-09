print("{:=^40}".format(" LOJAS MALG "))
preço = float(input("Preço das compras R$"))
print("""[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
print("  ")
opçao = int(input("Selecione a opção desejada: "))
print("   ")
if opçao == 1:
    total = preço - (preço * 10 / 100)
    print("Aplicando o o desconto...")
elif opçao == 2:
    total = preço - (preço * 5 / 100)
    print("Aplicando o o desconto...")
elif opçao == 3:
    total = preço
    parcela = preço / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparcelas = int(input("Quantas parcelas? "))
    parcela = total / totparcelas
    print("Sua compra será parcelada em {}x de R${:.2f} (COM JUROS)".format(totparcelas, parcela))
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total))
