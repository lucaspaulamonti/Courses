# Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.
def soma_matrizes(m1,m2):
    dim_m1=[len(m1),len(m1[0])]
    dim_m2=[len(m2),len(m2[0])]
    result=[]
    if(dim_m1==dim_m2):
        for(i)in(range(len(m1))):
            result.append([])
            for(j)in(range(len(m2))):
                x=((m1[i][j])+(m2[i][j]))
                result[i].append(x)
                return result
    else:
        return False
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!