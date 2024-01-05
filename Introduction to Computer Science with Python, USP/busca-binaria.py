# Crie uma função em python que utilize do algorítimo de busca binária para localizar número em lista ordenada.
def busca_sequencial(lista,x):
    for i in range(len(lista)):
        if lista[i]==x:
            return i
    return -1
    
def busca_binaria(lista,x):
    primeiro=0
    ultimo=len(lista)-1
    while primeiro<=ultimo:
        meio=(primeiro+ultimo)//2
        if lista[meio]==x:
            return meio
        else:
            if x < lista[meio]:
                ultimo=meio-1
            else:
                primeiro=meio+1
    return -1
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!