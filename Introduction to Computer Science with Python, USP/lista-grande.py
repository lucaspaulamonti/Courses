# Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma lista contendo n números inteiros aleatórios.
import random
import math
def lista_grande(n):
    count=0
    lista=[]
    while count<n:
        lista.append(math.ceil(100*random.random()))
        count+=1
    return lista
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!