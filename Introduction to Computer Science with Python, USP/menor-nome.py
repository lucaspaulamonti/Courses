# Escreva uma função menor_nome(nomes) que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.
def menor_nome(nomes):
    nomes_tratados=[]
    for(each_value)in(nomes):
        nomes_tratados.append(each_value.strip().capitalize())
    menor_nome=str(nomes_tratados[0])
    for(each_value)in(nomes_tratados):
        if(len(each_value))<(len(menor_nome)):
            menor_nome=each_value
    return menor_nome
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!