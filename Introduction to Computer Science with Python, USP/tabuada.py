# Faça um programa em Python que imprima as tabuadas do 1 ao 10 de forma tabelada.
linha=1
coluna=1
while(linha<=10):
    while(coluna<=10):
        print(linha*coluna,end='\t')
        coluna=coluna+1
    linha=linha+1
    print()
    coluna=1
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!