from datetime import date
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:   # != signififca diferente (no caso algo que seja diferente de 100)
    print("O ano {} é BISSEXTO.".format(ano))
else:
    print("O ano {} NÃO é BISSEXTO.".format(ano))