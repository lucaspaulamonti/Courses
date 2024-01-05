# Crie um menu com funções para cada item e armazene dados em arquivo de texto.
def listarArquivo(filename):
    try:
        mode=open(filename,'rt')
    except:
        print('Erro desconhecido')
    else:
        print(mode.read())
    mode.close
def cadastrarJogo(filename,nome_jogo,nome_game):
    try:
        mode=open(filename,'at')
    except:
        print('Erro desconhecido')
    else:
        mode.write('{},{}\n'.format(nome_jogo,nome_game))
    mode.close()
def createfile(filename):
    try:
        mode=open(filename,'wt+')
        mode.close()
    except:
        print('Erro desconhecido.')
        return False
    else:
        print('Nova DB foi criada.')
        return True
def fileexists(filename):
    try:
        mode=open(filename,'rt')
        mode.close()
    except FileNotFoundError:
        return False
    else:
        print('DB localizada.')
        return True
def realce(s1):
    if len(s1):
        print('+','-'*len(s1),'-','+')
        print('| ',s1,' |')
        print('+','-'*len(s1),'-','+')
def valida(q,min,max):
    x=int(input(q))
    while(x<min)or(x>max):
        x=int(input(q))
    return x
item=['1. Incluir','2. Filtrar','3. Sair']
file='db.txt'
if(fileexists(file)):
    next
else:
    print('DB inexistente.')
    createfile(file)
while(True):
    realce('Menu')
    print(item)
    select=valida('Escolha a opção desejada: ',1,3)
    if(select==1):
        print('Inclusão:')
        nome_jogo=input('Nome do jogo: ')
        nome_game=input('Nome do video-game: ')
        cadastrarJogo(file,nome_jogo,nome_game)
    elif(select==2):
        print('Filtro:')
        listarArquivo(file)
    elif(select==3):
        print('Encerrando.')
        break