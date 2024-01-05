# Utilize recursão para retornar os números ímpares de uma lista.
def encontra_impares(lista):
    lista_2=[]
    if len(lista)>0:
        if lista[0]%2==1:
            lista_2.extend([lista[0]])
        del(lista[0])
        lista_2+=encontra_impares(lista)
    return lista_2
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!