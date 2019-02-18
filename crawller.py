import urllib.request

#def getDolar():
content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) + len(find))
dolar = content[ posicao : posicao  + 4]
    #return dolar


print("Dolar: "+ dolar)
