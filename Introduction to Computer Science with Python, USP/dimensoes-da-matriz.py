# Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.
def dimensoes(matriz):
    dim=(len(matriz),len(matriz[0]))
    print('{}X{}'.format(dim[0],dim[1]))
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!