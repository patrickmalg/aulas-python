from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-' * 20)
num = int(input("Em que número eu pensei? "))
print("Processando")
sleep(3)
if num == comp:
    print("PARABÉNS! você conseguiu me vencer!!!")
else:   
    print("EU GANHEI!! Pensei em {} e não no {}.".format(comp, num))

