url = 'https://bytebank.com/cambio?moedaOrigem=real'

inIn = url.find('?')
urlB = url[0:inIn]
urlP = url[inIn + 1:]

print('Índice Interrogação: ', inIn)
print('URL Original: ', url)
print('URL Base: ', urlB)
print('URL Parâmetro: ', urlP)
