#RA ALUNO: 121127

#Escreva um programa que, dado o número
#total de eleitores votantes de um município,
#o número de votos brancos e o número de
#votos nulos, calcule os percentuais de votos
#válidos e total de brancos mais nulos que
#cada um representa em relação ao total de
#eleitores.


print("-" * 70)
print("OLÁ CIDADÃO, CONFIRA OS PERCENTUAIS DE VOTOS VÁLIDOS DE SEU MUNICÍPIO!")
print("-" * 70)
totVotos = int(input("Total de votos: "))
votosBr = int(input("Votos brancos: "))
votosNl = int(input("Votos nulos: "))
validos = totVotos - (votosBr + votosNl)
print("=" * 30)
print("TOTAL VOTOS: {}".format(totVotos))
print("VOTOS BRANCOS: {}".format(votosBr))
print("VOTOS NULOS: {}".format(votosNl))
print("VOTOS VÁLIDOS: {}".format(validos))
print("=" * 30)

calcValidos = 100 * validos / totVotos
calcBr = 100 * votosBr / totVotos
calcNl = 100 * votosNl / totVotos
nulosBrancos = votosBr + votosNl
totBrancosNulos = 100 * (votosBr + votosNl) / totVotos 

print("Percentual de votos válidos:  {} -> {:.2f}% ".format(validos, calcValidos))
print("Percentual de votos brancos: {} -> {:.2f}%".format(votosBr,calcBr))
print("Percentual de votos nulos: {} -> {:.2f}%".format(votosNl, calcNl))
print("Percentual de brancos E nulos: {} -> {:.2f}%".format(nulosBrancos,totBrancosNulos))

