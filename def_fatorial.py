def fatorial(f):
    r = f
    for i in range(2, f):
        r*= i
num = int(input("Digite um número para ver seu fatorial: "))
print("O fatorial de {} é. ".format(num), fatorial(num))