# Implemente a função ordena(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize o algoritmo selection sort.
def ordena(list):
    size=len(list)
    for(step)in(range(size)):
        min_idx=step
        for(i)in(range(step+1,size)):
            if(list[i])<(list[min_idx]):
                min_idx=i
        (list[step],list[min_idx])=(list[min_idx],list[step])
    return list
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!