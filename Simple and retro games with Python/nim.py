# Faça um programa em Python que simule um jogo do Nim usuário-cpu.
# campeonato
def campeonato():
    turno=1
    while(turno<=3):
        print('****rodada',turno,'****')
        partida()
        turno+=1
    print('**** final do campeonato! ****')
    print('placar: você 0 x 3 computador')
# //campeonato
# computador_escolhe_jogada
def computador_escolhe_jogada(numerodepecas,maximodepecas):
    removidascomputador=1
    while(removidascomputador!=maximodepecas):
        if(numerodepecas-removidascomputador)%(maximodepecas+1)==0:
            return removidascomputador
        else:
            removidascomputador+=1
    return removidascomputador
# //computador_escolhe_jogada
# usuario_escolhe_jogada
def usuario_escolhe_jogada(numerodepecas,maximodepecas):
    chave=True
    while(chave==True):
        removidasusuario=int(input('quantas peças você vai tirar?'))
        if(removidasusuario>maximodepecas)or(removidasusuario<1):
            print('oops! jogada invalida! tente de novo')
        else:
            chave=False
    return removidasusuario
# //usuario_escolhe_jogada
# partida
def partida():
    numerodepecas=int(input('quantas peças?'))
    maximodepecas=int(input('limite de peças por jogada?'))
    # removidascomputador=()
    # removidasusuario=()
    chave=True
    if((numerodepecas%(maximodepecas+1))==0):
        print('voce começa!')
    else:
        print('computador começa!')
        chave=False
    while(numerodepecas>0):
        if(chave==False):
            removidascomputador=(computador_escolhe_jogada(numerodepecas,maximodepecas))
            numerodepecas=(numerodepecas-removidascomputador)
            if(removidascomputador==1):
                print('o computador tirou uma peça')
            else:
                print('o computador tirou',removidascomputador,'peças')
            chave=True
        else:
            removidasusuario=(usuario_escolhe_jogada(numerodepecas,maximodepecas))
            numerodepecas=numerodepecas-removidasusuario
            if(removidasusuario==1):
                print('você tirou uma peça')
            else:
                print('você tirou',removidasusuario,'peças')
            chave=False
        if(numerodepecas==1):
            print('agora resta apenas uma peça no tabuleiro')
        else:
            if(numerodepecas!=0):
                print('agora restam',numerodepecas,'peças no tabuleiro')
    print('fim do jogo! o computador ganhou!')
# //partida
# inicio
tipodejogo=str()
print('bem-vindo ao jogo do nim! escolha:')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')
tipodejogo=str(input())
if(tipodejogo==str('1')):
    print('você escolheu uma partida isolada')
    partida()
elif(tipodejogo==str('2')):
    print('você escolheu um campeonato')
    campeonato()
elif(tipodejogo==str('egg')):
    print('nao tem nenhum easter egg aqui')
else:
    quit()
# /inicio