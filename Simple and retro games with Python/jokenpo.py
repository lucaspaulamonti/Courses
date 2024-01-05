import random
import time
import os
clearConsole=lambda:os.system('cls'if os.name in('nt','dos')else'clear')
def result(userChoice,cpuChoise):
    print('Você jogou:',userChoice,'.')
    print('CPU jogou:',cpuChoise,'.')
    print()
def jokenpo():
    list=['Pedra','Papel','Tesoura']
    call=['JO-',' KEN ','  -PÔ']
    key=bool(True)
    userChoice=str()
    cpuChoise=str()
    while key==True:
        print('Selecione uma opção para jogar:')
        print('[1]',list[0],',','[2]',list[1],'ou [3]',list[2],'.')
        userChoice=str(input('> '))
        if((userChoice=='1')or(userChoice=='2')or(userChoice=='3')):
            clearConsole()
            break
        else:
            print('Ops! Você precisa informar 1, 2 ou 3.')
            print('Tente novamente.')
            time.sleep(1)
            clearConsole()
    cpuChoise=random.choice(list)
    for(i)in call:
        print(i)
        time.sleep(1)
    clearConsole()
    if(userChoice=='1'):
        userChoice=list[0]
    elif(userChoice=='2'):
        userChoice=list[1]
    else:
        userChoice=list[2]
    if userChoice==cpuChoise:
        result(userChoice,cpuChoise)
        print('Vocês empataram!')
    elif((userChoice==list[0])and(cpuChoise==list[1]))or((userChoice==list[1])and(cpuChoise==list[2]))or((userChoice==list[2])and(cpuChoise==list[0])):
        result(userChoice,cpuChoise)
        print('Você perdeu!')
    else:
        result(userChoice,cpuChoise)
        print('Você ganhou!')
    print('Pressione qualquer tecla para sair.')
    input('> ')
iniciar=str('isNull')
clearConsole()
print('Bem-vindo ao JO-KEN-PÔ!')
while iniciar==str('isNull'):
    print('Pressione qualquer tecla para iniciar.')
    iniciar=str(input('> '))
clearConsole()
jokenpo()

