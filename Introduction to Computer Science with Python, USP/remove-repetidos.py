# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
def remove_repetidos(list):
    newlist=[]
    list.sort()
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!