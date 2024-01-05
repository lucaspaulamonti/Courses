import random
import time
import os
import math
clearConsole=lambda:os.system('cls'if os.name in('nt','dos')else'clear')
def dot_effect():
    count=int(0)
    while(count<10):
        count+=1
        if(count==1)or(count==4)or(count==7)or(count==10):
            dot='.'
        elif(count==2)or(count==5)or(count==8):
            dot='..'
        else:
            dot='...'
        print('Sorteando as opções',dot)
        time.sleep(0.5)
        clearConsole()
iniciar=str('')
options=['Par','Impar']
userOption=random.choice(options)
cpuOption=int()
userChoice=str()
cpuChoise=math.ceil(100*random.random())
clearConsole()
dot=str('')
result=int()
par_impar=str('')
print('Bem-vindo ao Par ou Impar!')
print('Pressione Enter para iniciar.')
iniciar=str(input('> '))
clearConsole()
dot_effect()
print('Usuário é: ',userOption,'.')
if('Par'!=userOption):
    cpuOption='Par'
else:
    cpuOption='Impar'
print('CPU é: ', cpuOption,'.')
while(userChoice.isnumeric()!=True):
    print('Jogue um número inteiro.')
    userChoice=str(input('> '))
    if(userChoice.isnumeric()):
        userChoice=int(userChoice)
        clearConsole()
        break
    else:
        print('Entrada inválida.')
        time.sleep(0.5)
        clearConsole()
print('Usuário jogou: ',userChoice,'.')
time.sleep(0.5)
print('CPU jogou: ',cpuChoise,'.')
time.sleep(0.5)
result=userChoice+cpuChoise
print('Resultado:',result)
time.sleep(0.5)
if(result)%2==0:
    print('É Par.')
    par_impar=options[0]
else:
    print('É Impar.')
    par_impar==options[1]
if(userOption==par_impar):
    print('Usuário ganhou!')
else:
    print('CPU ganhou!')
print('Pressione Enter para finalizar.')
iniciar=str(input('> '))