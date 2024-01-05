# Escreva um algorítimo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada palavra, faça um print na tela com o nome da palavra e suas respectivas vogais.
palavra=('Mario','Luigi','Peach','Yoshi','Bowser')
for each in palavra:
    print('\nPalavra: {}.\nVogais:'.format(each.upper()),end=' ')
    for i in each:
        if i.lower() in 'aeiou':
            print(i.upper(),end=' ')