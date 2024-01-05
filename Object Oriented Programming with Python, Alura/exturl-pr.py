# url: Armazena a url original.
url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar'

# Sanitização.
# Se url é vazio.
url = url.strip()
if url == '':
    raise ValueError('A url é vazia.')

# inIn: Encontra o índice: ?.
# urlB: Armazena a url base.
# urlP: Armazena os parâmetros.
inIn = url.find('?')
urlB = url[0:inIn]
urlP = url[inIn + 1:]

print('URL Original: ', url)
print('Índice ?: ', inIn)
print('URL Base: ', urlB)
print('URL Parâmetro: ', urlP)

# buscaParam: Armazena o parâmetro que será buscado.
# inBuscaParam: Encontra o índice do parâmetro que será buscado.
buscaParam = 'moedaOrigem'
inBuscaParam = urlP.find(buscaParam)

print('Parâmetro: ', buscaParam)
print('Índice do Parâmetro: ', inBuscaParam)

# inVal: Encontra o índice do valor do parâmetro buscado.
# inE: Encontra o índice: &.
# val: Armazena o valor do parâmetro buscado.
inVal = inBuscaParam + len(buscaParam) + 1
inE = urlP.find('&', inVal)

# Se não existir &, busca até o fim.
# Se existir &, busca até ele.
if inE == -1:
    val = urlP[inVal:]
else:
    val = urlP[inVal:inE]

print('Índice do Valor:', inVal)
print('Índice &: ', inE)
print('Valor: ', val)

