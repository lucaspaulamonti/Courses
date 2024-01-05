# Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo insertion sort.
def insertion_sort(lista):
    lst=[]
    for i in range(1, len(lista)):
        key=lista[i]
        j=i-1
        while j>=0 and key<lista[j]:
                lista[j+1] = lista[j]
                j-=1
        lista[j+1]=key
    for i in range(len(lista)):
        lst.append(lista[i])
    return lst
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!