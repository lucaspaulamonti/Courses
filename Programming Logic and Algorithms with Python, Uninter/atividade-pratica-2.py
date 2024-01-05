# Questão 2.
# Identificação.
def identificacao():
    lucasdepaulamonti_4170082='Lucas de Paula Monti'
    print('Seja bem-vindo a pizzaria do {}.'.format(lucasdepaulamonti_4170082))

# cardapio.
def cardapio():
    print('+---------------Cardápio------------------+')
    print('| Código | Descrição  | Pizza M | Pizza G |')
    print('| 21     | Napolitana | R$20.00 | R$26.00 |')
    print('| 22     | Margherita | R$20.00 | R$26.00 |')
    print('| 23     | Calabresa  | R$25.00 | R$32.50 |')
    print('| 24     | Toscana    | R$30.00 | R$39.00 |')
    print('| 25     | Portuguesa | R$30.00 | R$39.00 |')
    print('+-----------------------------------------+')

# validaInt.
def validaInt(q,min,max):# valida se usuário digitou 0 ou 1.
    while(True):
        try:
            x=int(input(q))
            while(((x)<(min))or((x)>(max))):
                entradaInvalida()
                x=int(input(q))
            return x
        except:
            entradaInvalida()
            
# entradaInvalida.
def entradaInvalida():
    print('Opção Inválida.')

# calculoValor.
def calculoValor(sub):
    while(True):
        tam=input('Qual é o tamanho desejado [M/G]? > ')
        if((tam=='M')or(tam=='G')):# aceita apenas valor M ou G.
            try:
                cod=int(input('Qual é o código do sabor desejado? >'))
                if(cod==21):# Napolitana.
                    res='Napolitana'
                    if(tam=='M'):# preço do M.
                        sub=20
                    else:# preço do G.
                        sub=26
                elif(cod==22):# Margherita.
                    res='Margherita'
                    if(tam=='M'):# preço do M.
                        sub=20
                    else:# preço do G.
                        sub=26
                elif(cod==23):# Calabresa.
                    res='Calabresa'
                    if(tam=='M'):# preço do M.
                        sub=25
                    else:# preço do G.
                        sub=32.5
                elif(cod==24):# Toscana.
                    res='Toscana'
                    if(tam=='M'):# preço do M.
                        sub=30
                    else:# preço do G.
                        sub=39
                elif(cod==25):# Portuguesa.
                    res='Portuguesa'
                    if(tam=='M'):# preço do M.
                        sub=30
                    else:# preço do G.
                        sub=39
                else:
                    entradaInvalida()
                    continue
                print('Você pediu uma pizza sabor: {}, tamanho: {}'.format(res,tam))
                return sub
            except:
                entradaInvalida() 
                continue
        else:
            entradaInvalida()
            continue

# Main.
identificacao()
cardapio()
sub=float(0)
while(True):
    sub+=calculoValor(sub)
    acr=validaInt('Deseja pedir mais alguma coisa?\n1. Sim\n0. Não\n> ',0,1)
    if(acr==1):
        continue
    else:
        print('O total a ser pago é R${:.2f}'.format(sub))
        break