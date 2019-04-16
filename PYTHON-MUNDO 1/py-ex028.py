vCarro = float(input("Qual a velocidade atual do carro? "))
if vCarro > 80:
    print("MUTADO! Você excedeu o limite permitido de 80Km/h")
    multa = (vCarro - 80) * 7
    print("Por estar em uma velocidade de {}Km/h, você deve pagar uma multa de R${:.2f}!".format(vCarro, multa))
print("Bom dia! Seja consciênte e dirija o seu carro com segurança seu BABACA.")


