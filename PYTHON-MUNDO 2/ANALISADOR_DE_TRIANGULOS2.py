print("-=-" * 20)
print("ANALISADOR DE TRIÂNGULOS 2")
print("-=-" * 20)

r1 = float(input("Pirmeiro segmento: "))
r2 = float(input("Segundo seguimento: "))
r3 = float(input("Terceiro segmento: "))

#EQUILÁTERO: TODOS LADOS IGUAIS
#ISÓCELES: DOIS LADOS IGUAIS
#ESCALENO: TODOS OS LADOS DIFERENTES

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos FORMAM um triângulo!")
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("Os segmentos NÃO formam um triângulo!")



