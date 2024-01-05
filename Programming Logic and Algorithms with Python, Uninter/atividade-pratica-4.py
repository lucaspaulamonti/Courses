# Questão 4.
produserviList=list()
proserCodigo=int(0)

# Identificação.
def identificacao():
    lucasdepaulamonti_4170082='Lucas de Paula Monti'
    print('Seja bem-vindo a Controle de Estoque do {}.'.format(lucasdepaulamonti_4170082))

# removerProduto.
def removerProduto():
    print('Exclusão de Produtos:')
    while(True):
        try:
            print('Excluíndo por CÓDIGO.')
            entry=int(input('Informe o Código:\n> '))
            for(produto)in(produserviList):
                if(produto['proserCodigo']==(entry)):
                    produserviList.remove(produto)
                    return
        except:
            print('Erro desconhecido.')
            continue
        print('Código não localizado.')
        return

# consultarProduto.
def consultarProduto():
       while(True):
        try:
            print('Consulta de Produtos:')
            opce=validaInt(
            'Informe a opção desejada.\n'
            '1. Consultar todos.\n'
            '2. Consultar por CÓDIGO.\n'
            '3. Consultar por FABRICANTE.\n'
            '4. Retornar.\n> ',1,4
            )
            if((opce)==(int(1))):
                print('Consultando todos.')
                for(produto)in(produserviList):
                    for(key,value)in(produto.items()):
                        print('{}: {}'.format(key,value))
            elif((opce)==(int(2))):
                while(True):
                    try:
                        print('Consultando por Código.')
                        entry=int(input('Informe o Código:\n> '))
                        for(produto)in(produserviList):
                            if(produto['proserCodigo']==(entry)):
                                for(key,value)in(produto.items()):
                                    print('{}: {}'.format(key,value))
                                return
                    except:
                        print('Erro desconhecido.')
                        continue
                    print('Código não localizado.')
                    return
            elif((opce)==(int(3))):
                while(True):
                    try:
                        print('Consultando por FABRICANTE.')
                        entry=input('Informe a Fabricante:\n> ').upper()
                        for(produto)in(produserviList):
                            if(produto['fabricanteProduto']==(entry)):
                                for(key,value)in(produto.items()):
                                    print('{}: {}'.format(key,value))
                        return
                    except:
                        print('Erro desconhecido.')
                        continue
            else:
                return
        except:
            print('Erro desconhecido.')
            continue

# cadastrarProduto.
def cadastrarProduto(proserCodigo):
    print('Cadastro de Produtos:')
    print('Código do Produto: {}'.format(proserCodigo))
    nomeProduto=input('Informe o NOME do produto: ').upper()
    fabricanteProduto=input('Informe a FABRICANTE do produto: ').upper()
    valorProduto=float(input('Informe o VALOR do produto: R$'))
    produservi=dict({
    'proserCodigo':proserCodigo,
    'nomeProduto':nomeProduto,
    'fabricanteProduto':fabricanteProduto,
    'valorProduto':valorProduto
    })
    produserviList.append(produservi.copy())

# validaInt.
def validaInt(q,min,max):
    x=int(input(q))
    while(((x)<(min))or((x)>(max))):
        x=int(input(q))
    return x

# Main.
identificacao()
while(True):
    try:
        op=int(validaInt(
        'Informe a opção desejada.\n'
        '1. Cadastro\n'
        '2. Filtro\n'
        '3. Exclusão\n'
        '4. Sair\n> ',1,4
        ))
        if((op)==(int(1))):
            proserCodigo+=1
            cadastrarProduto(proserCodigo)
        elif((op)==(int(2))):
            consultarProduto()
        elif((op)==(int(3))):
            removerProduto()
        else:
            break
    except:
        print('Erro desconhecido.')
        continue