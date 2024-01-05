# Questão 3.
# Identificação.
def identificacao():
    lucasdepaulamonti_4170082='Lucas de Paula Monti'
    print('Seja bem-vindo a Feijoaderia do {}.'.format(lucasdepaulamonti_4170082))

# validaInt.
def validaInt(q,min,max):# valida se usuário digitou 0 ou 1.
    while(True):
        try:
            x=int(input(q))
            while(((x)<(min))or((x)>(max))):
                print('Informe um valor válido.')
                x=int(input(q))
            return x
        except:
            print('Informe um valor válido.')

# volumeFeijoada.
def volumeFeijoada():
    while(True):
        try:
            volumeMls=float(input('Informe a quantidade de ml\'s desejados: > '))
            if(300<=volumeMls<=5000):
                valorVolume=(volumeMls*0.08)
                return valorVolume
            print('Não aceitamos porções menores que 300ml ou maiores que 5l.')
        except:
            print('Por favor, informe um valor numérico.')

# opcaoFeijoada.
def opcaoFeijoada():
    while(True):
        opcaoDesejada=input('Informe a opção desejada:\nb - Básica (Feijão + paiol + costelinha)\np - Premium (Feijão + paiol + costelinha + partes de porco)\ns - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\n> ')
        if(opcaoDesejada=='b'):
            multiplicador=1
        elif(opcaoDesejada=='p'):
            multiplicador=1.25
        elif(opcaoDesejada=='s'):
            multiplicador=1.5
        else:
            print('Você não digitou uma opção válida.')
            continue
        return multiplicador

# acompanhamentoFeijoada.
def acompanhamentoFeijoada():
    resultadoAc=float(0)
    while(True):
        acDesejado=validaInt('Deseja mais algum acompanhamento?\n0- Não desejo mais acompanhamentos (encerrar pedido)\n1- 200g de arroz\n2- 150g de farofa especial\n3- 100g de couve cozida\n4- 1 laranja descascada\n> ',0,4)
        if(acDesejado==0):
            resultadoAc+=0
            return resultadoAc
        elif(acDesejado==1):
            resultadoAc+=5
        elif(acDesejado==2):
            resultadoAc+=6
        elif(acDesejado==3):
            resultadoAc+=7
        else:
            resultadoAc+=3

# Main.
identificacao()
print('Menu: Volume da Feijoada.')
vol=volumeFeijoada()
print('Menu: Opção da Feijoada.')
op=opcaoFeijoada()
print('Menu: Acompanhamento da Feijoada.')
ac=acompanhamentoFeijoada()
print('O valor a ser pago é de: R${:.2f}. (Volume: {:.2f} * Opção: {:.2f} + Acompanhamentos: {:.2f}).'.format(((vol*op)+ac),vol,op,ac))