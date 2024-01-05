# Implemente a função bolha(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize o algoritmo bubble sort.
def bolha(lista):
    fim=len(lista)
    for(i)in(range(fim-1,0,-1)):
        for(j)in(range(i)):
            if(lista[j])>(lista[j+1]):
                (lista[j]),(lista[j+1])=(lista[j+1]),(lista[j])
    return lista
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!