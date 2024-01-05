class Conta:
    def __init__(self,num, tit, sal, lim):
        print('\nCriando a sua conta...')
        print('Endereço de memória alocado:')
        print(self)
        self.__num = num
        print('Gravando o número...')
        print('Número informado: {}'.format(self.__num))
        self.__tit = tit
        print('Gravando o titular...')
        print('Titular informado: {}'.format(self.__tit))
        self.__sal = sal
        print('Gravando o saldo...')
        print('Saldo informado: {}'.format(self.__sal))
        self.__lim = lim
        print('Gravando o limite...')
        print('Limite informado: {}'.format(self.__lim))
        print('\nA sua conta foi criada:')
        print('Número: {}'.format(self.__num))
        print('Titular: {}'.format(self.__tit))
        print('Saldo: {}'.format(self.__sal))
        print('Limite: {}\n'.format(self.__lim))

    def ext(self):
        print('\nConsultando o seu saldo...')
        print('Saldo do titular {}: R${}\n'.format(self.__tit, self.__sal))

    def cre(self, val):
        self.__sal += val
        print('\nCreditando o valor...')
        print('Foram creditados: R${}'.format(val))
        print('Novo saldo: R${}\n'.format(self.__sal))

    def deb(self, val):
        self.__sal -= val
        print('\nDebitando o valor...')
        print('Foram debitados: R${}'.format(val))
        print('Novo saldo: R${}\n'.format(self.__sal))

    def tra(self, des, val):
        print('\nTranferindo R${} para {}.'.format(val, des.__tit))
        self.deb(val)
        des.cre(val)

