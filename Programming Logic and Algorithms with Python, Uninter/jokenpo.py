# Crie um jogo de pedra, papel ou tesoura.
import random
def vencedor(j1,j2):
    global e,v1,v2
    if(j1==1):
        if(j2==1):
            e+=1
        elif(j2==2):
            v2+=1
        else:
            v1+=1
    elif(j1==2):
        if(j2==1):
            v1+=1
        elif(j2==2):
            e+=1
        else:
            v2+=1
    else:
        if(j2==1):
            v2+=1
        elif(j2==2):
            v1+=1
        else:
            e+=1
    resultado=[v1,v2,e]
    return resultado
def valida(q,min,max):
    x=int(input(q))
    while(x<min)or(x>max):
        x=int(input(q))
    return x
print('Jokenpo\n1. Pedra, 2. Papel ou 3. Tesoura.')
j=[]
r=[]
v1=0
v2=0
e=0
while(True):
    j1=valida('Escolha sua jogada: ',0,3)
    if not j1:
        break
    j2=random.randint(1,3)
    j.append([j1,j2])
    r=vencedor(j1,j2)
    print(r)
print(r[0],' vitórias do jogador 1.')