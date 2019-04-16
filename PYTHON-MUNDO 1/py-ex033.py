print("-=-" * 20)
print("ANALISADOR DE TRIÂNGULOS")
print("-=-" * 20)
r1 = float(input("Pirmeiro segmento: "))
r2 = float(input("Segundo seguimento: "))
r3 = float(input("Terceiro segmento: "))

if r1 > (r2 + r3):
    print("Os seguimentos NÃO formam um triângulo!")
elif r2 > (r1 + r3):
    print("Os seguimentos NÃO formam um triângulo!")
elif r3 > (r1 + r2):
     print("Os seguimentos NÃO formam um triângulo!")
else:
    print("Os segmentos FORMAM um triângulo!")