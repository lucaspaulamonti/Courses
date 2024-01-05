# Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.
def maiusculas(frase):
    letras_maiusculas=str()
    for(each)in(frase):
        if((ord(each)>64)and(ord(each)<91)):
            letras_maiusculas+=each
    return letras_maiusculas
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!