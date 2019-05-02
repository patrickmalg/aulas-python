from random import randint
computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Chute mais alto... ")
        elif jogador > computador:
            print("Menos... está quase! ")
print("Acertou com {} tentavivas, parabéns!".format(palpites))
