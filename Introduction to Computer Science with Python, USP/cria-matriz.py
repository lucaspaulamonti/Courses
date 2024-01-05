# Escreva uma função que cria uma matriz com determinados valores informados.
def cria_matriz(lin,col):
    matriz=[]
    for(each_lin)in(range(lin)):
        linha=[]
        for(each_col)in(range(col)):
            value=int(input('Informe o elemento ['+str(each_lin)+']['+str(each_col)+']: '))
            linha.append(value)
        matriz.append(linha)
    return matriz
def le_matriz():
    lin=int(input('Informe o número de linhas da matriz: '))
    col=int(input('Informe o número de colunas da matriz: '))
    return cria_matriz(lin,col)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!