# Faça um programa em Python que dada uma lista de temperatura com dados do mês, informar a mais fria e mais quente.
def MinMax(temperatura):
    print('A MENOR temperatura do mês foi: ',minima(temperatura),'C.')
    print('A MAIOR temperatura do mês foi: ',maxima(temperatura),'C.')
def maxima(temp):
    max=temp[0]
    i=1
    while(i<len(temp)):
        if temp[i]>max:
            max=temp[i]
        i+=1
    return max
def minima(temp):
    min=temp[0]
    i=1
    while(i<len(temp)):
        if temp[i]<min:
            min=temp[i]
        i+=1
    return min
def testPontual(temp,valorEsperado):
    valorCalculado=minima(temp)
    if valorCalculado!=valorEsperado:
        print('Valor errado para array ',temp)
        print('Valor esperado: ',valorEsperado)
        print('Valor calculado: ',valorCalculado)
def testMinima():
    print('Iniciando os testes.')
    testPontual([0],0)
    testPontual([0,0,0,0,0],0)
    testPontual([0,1,2,3,4,5,6,7,8,9,10],0)
    testPontual([-1,0,1],-1)
    print('Finalizando os testes.')
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!