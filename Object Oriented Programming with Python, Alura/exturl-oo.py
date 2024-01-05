class ExtUrl:
    def __init__(self, url):
        self.url = self.stzUrl(url)
        self.vldUrl()

    def stzUrl(self, url):
        return url.strip()

    def vldUrl(self):
        if self.url == '':
            raise ValueError('A url é vazia.')

    def getUrlB(self):
        inIn = self.url.find('?')
        urlB = self.url[0:inIn]
        return urlB

    def getUrlP(self):
        inIn = self.url.find('?')
        urlP = self.url[inIn + 1:]
        return urlP

    def getBuscaParam(self, buscaParam):
        inBuscaParam = self.getUrlP().find(buscaParam)
        inVal = inBuscaParam + len(buscaParam) + 1
        inE = self.getUrlP().find('&', inVal)
        if inE == -1:
            val = self.getUrlP()[inVal:]
        else:
            val = self.getUrlP()[inVal:inE]
        return val

extUrl = ExtUrl('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar')
moedaOrigem = extUrl.getBuscaParam('moedaOrigem')
print(moedaOrigem)
