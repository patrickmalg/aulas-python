#Escreva um método que aceite um valor
#inteiro (x) como parâmetro e calcule a
#expressão:


tempo = int(input("Digita um valor: "))
dias = tempo / 86400
resto = tempo % 86400

horas = resto / 3600
restoHoras = resto % 3600

minutos = restoHoras / 60
restoMinutos = resto % 60

segundos = tempo % 60

print("Convertendo o valor de {} segundos: {:.0f} Dias, {:.0f} horas, {:.0f} minutos e {:.0f} segundos.".format(tempo, dias, horas, minutos, segundos)) 

