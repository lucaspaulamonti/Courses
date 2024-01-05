# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.
def maximo(a,b,c):
    if a>b and a>c:
        return a
    if b>c and b>a:
        return b    
    if c>a and c>b:
        return c
    if a==b and a==c:
        return a    
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!