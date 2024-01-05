# Armazene cadastro de clientes em um dicionário e calcule os totalizadores pedidos.
cliforn={'cliforn.nome':[],'cliforn.sexo':[],'cliforn.dtnasc':[]}
while(True):
    y=input('Incluir? [s/n]:\n > ').upper()
    if((y)in('N')):
        break
    elif((y)not in('S')):
        print('Erro desconhecido.')
        continue
    else:
        nome=input('Qual o seu nome?\n > ').upper()
        if(len(nome)==0):
            print('Erro desconhecido.')
            continue
        sexo=input('Qual o seu sexo?\n > ').upper()
        if(len(sexo)==0):
            print('Erro desconhecido.')
            continue
        try:
            dtnasc=int(input('Qual seu ano de nascimento?\n > '))
            if(dtnasc<1900)or(dtnasc>2022):
                print('Erro desconhecido.')
                continue
        except:
            print('Erro desconhecido.')
            continue
        cliforn['cliforn.nome'].append(nome)
        cliforn['cliforn.sexo'].append(sexo)
        cliforn['cliforn.dtnasc'].append(dtnasc)
print(cliforn)