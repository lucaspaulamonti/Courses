# Elabore um cadastro de estudantes com inclusão, consulta e exclusão.
listaEstudantes=list()
registroAcademico=int(0)
def validaInt(q,min,max):
    x=int(input(q))
    while(((x)<(min))or((x)>(max))):
        x=int(input(q))
    return x
def removerEstudante():
    print('Exclusão de Estudantes:')
    while(True):
        try:
            print('Excluíndo por RU.')
            entry=int(input('Informe o RU:\n> '))
            for(estudante)in(listaEstudantes):
                if(estudante['registroAcademico']==(entry)):
                    listaEstudantes.remove(estudante)
                    return
        except:
            print('Erro desconhecido.')
            continue
        print('RU não localizado.')
        return
def consultarEstudante():
    while(True):
        try:
            print('Consulta de Estudantes:')
            opce=validaInt(
            'Informe a opção desejada.\n'
            '1. Consultar todos.\n'
            '2. Consultar por RU.\n'
            '3. Consultar por TURMA.\n'
            '4. Retornar.\n> ',1,4
            )
            if((opce)==(int(1))):
                print('Consultando todos.')
                for(estudante)in(listaEstudantes):
                    for(key,value)in(estudante.items()):
                        print('{}: {}'.format(key,value))
            elif((opce)==(int(2))):
                while(True):
                    try:
                        print('Consultando por RU.')
                        entry=int(input('Informe o RU:\n> '))
                        for(estudante)in(listaEstudantes):
                            if(estudante['registroAcademico']==(entry)):
                                for(key,value)in(estudante.items()):
                                    print('{}: {}'.format(key,value))
                                return
                    except:
                        print('Erro desconhecido.')
                        continue
                    print('RU não localizado.')
                    return
            elif((opce)==(int(3))):
                while(True):
                    try:
                        print('Consultando por TURMA.')
                        entry=input('Informe a TURMA:\n> ').upper()
                        for(estudante)in(listaEstudantes):
                            if(estudante['turmaEstudante']==(entry)):
                                for(key,value)in(estudante.items()):
                                    print('{}: {}'.format(key,value))
                                return
                    except:
                        print('Erro desconhecido.')
                        continue
                    print('TURMA não localizada.')
                    return
            else:
                return
        except:
            print('Erro desconhecido.')
            continue
def cadastrarEstudante(registroAcademico):
    print('Cadastro de Estudantes:')
    print('Registro Acadêmico: {}'.format(registroAcademico))
    nomeEstudante=input('Informe o NOME do estudante: ').upper()
    turmaEstudante=input('Informe a TURMA do estudante: ').upper()
    dadosEstudante=dict({
    'registroAcademico':registroAcademico,
    'nomeEstudante':nomeEstudante,
    'turmaEstudante':turmaEstudante
    })
    listaEstudantes.append(dadosEstudante.copy())
print('Controle de Estudantes:')
while(True):
    try:
        op=validaInt(
        'Informe a opção desejada.\n'
        '1. Cadastro\n'
        '2. Filtro\n'
        '3. Exclusão\n'
        '4. Sair\n> ',1,4
        )
        if((op)==(int(1))):
            registroAcademico+=1
            cadastrarEstudante(registroAcademico)
        elif((op)==(int(2))):
            consultarEstudante()
        elif((op)==(int(3))):
            removerEstudante()
        else:
            break
    except:
        print('Erro desconhecido.')
        continue