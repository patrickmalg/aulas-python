def Soma(n1, n2):
    return float(n1) + float(n2)
def Divisao(n1, n2):
    return float(n1)/float(n2)
def Multiplicacao(n1, n2):
  return float(n1) * float(n2)
def Subtracao(n1, n2):
  return float(n1)-float(n2)

while (True):
  print("""1 - soma
2 - divisão
3 - multiplicação
4 - subtração""")
  operador = str(input("selecione uma opção: "))
  numero1 = input("Digite o primeiro numero: ")
  numero2 = input("Digite o segundo numero: ")
  if operador == "1":
    print("Resultado", Soma(numero1,numero2))
    break;
  elif operador == "2":
    print("Resultado", Divisao(numero1, numero2))
    break;
  elif operador == "3":
    print("Resultado", Multiplicacao(numero1, numero2))
    break;
  elif operador == "4":
    print("Resultado", Subtracao(numero1,numero2))
    break;
  else:
    print("Digite uma entrada válida!")


  





