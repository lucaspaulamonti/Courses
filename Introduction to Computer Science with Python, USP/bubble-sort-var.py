# Variação do algorítimo bubble sort.
def bolha(lista):
    fim=len(lista)
    for(i)in(range(fim-1,0,-1)):
        change=False
        for(j)in(range(i)):
            if(lista[j])>(lista[j+1]):
                (lista[j]),(lista[j+1])=(lista[j+1]),(lista[j])
                change=True
        if not change:
            return lista
    return lista
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!