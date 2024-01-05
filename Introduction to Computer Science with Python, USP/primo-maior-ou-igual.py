# Escreva uma função que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número.
def primo(n):
    i=n-1
    while i>0:
        if i==1:
            return True
            break
        elif(n%i == 0):
            return False
            break
        else:
            i-=1
def maior_primo(a):
    while a>0:
        if primo(a)==True:
            return a
            break
        else:
            a-=1
    return a
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!