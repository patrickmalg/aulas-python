termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimoTermo = termo + (10 - 1) * razao
for c in range(termo, decimoTermo, razao):
    print("{} ".format(c), end="→ ")
print("Fim")
