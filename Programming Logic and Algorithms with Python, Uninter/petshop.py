# Crie um sistema para um petshop segundo parâmetros solicitados.
# Função: servicocao(): Início.
def servicoCao():
    while(True):
        servicoC=input('Escolha o serviço desejado:\nBA. Banho\nTO. Tosa\nBT. Banho e Tosa\n> ')
        if(servicoC==str('BA')):
            return 10.00
        elif(servicoC==str('TO')):
            return 20.00
        elif(servicoC==str('BT')):
            return 25.00
        else:
            print('Erro desconhecido.')
# Função: servicocao(): Fim.
# Função: pesocao(): Início.
def pesoCao():
    while(True):
        try:
            pesoC=float(input('Informe o peso do cachorro (kg)\n> '))
            if(0<=pesoC<=10):
                return 1.5
            elif(10<pesoC<=20):
                return 2.0
            elif(20<pesoC<=30):
                return 2.5
            elif(30<pesoC<=40):
                return 3.0
            elif(40<pesoC):
                return 4.0
            else:
                print('Erro desconhecido.')
        except:
            print('Erro desconhecido.')
# Função: pesocao(): Fim.
# Função: pelocao(): Início.
def peloCao():
    while(True):
        peloC=input('Informe o pelo do cachorro:\nCU. Curto\nME. Médio\nLO. Longo\n> ')
        if(peloC==str('CU')):
            return 1.5
        elif(peloC==str('ME')):
            return 2.0
        elif(peloC==str('LO')):
            return 2.5
        else:
            print('Erro desconhecido.')
    return
# Função: pelocao(): Fim.
# Main.
print('Bem-vindo ao PetShop do Lucas.')
print('O valor total foi de: R${:.2f}'.format(servicoCao()*pesoCao()*peloCao()))