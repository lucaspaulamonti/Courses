import random


def importaPalavra():
    file = open("palavra.txt", "r")
    palavraImportada = []
    for linha in file:
        palavraImportada.append(linha.strip().upper())
    file.close()
    return palavraImportada[random.randrange(0, len(palavraImportada))]

def imprimeLetrAcertada(palavraSecreta):
    return ['_' for letra in palavraSecreta]

def scanner():
    return str.strip(str.upper(input('Escolha uma letra.\n> ')))

def registraLetra(palavraSecreta, chute, letrAcertada):
    posicao = 0
    for letra in palavraSecreta:
        if chute == letra:
            print('Encontrei a letra {} na posição {}.'.format(letra, posicao + 1))
            letrAcertada[posicao] = letra
        else:
            pass
        posicao += 1
    return

def resultado(acertou, palavraSecreta):
    if acertou:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    print('A palavra era: {}'.format(palavraSecreta))
    print('Fim de jogo.')
    return

def loop(palavraSecreta):
    letrAcertada = imprimeLetrAcertada(palavraSecreta)
    print(letrAcertada)
    enforcou, acertou = False, False
    erro = 0
    while not enforcou and not acertou:
        chute = scanner()
        if chute in palavraSecreta:
            registraLetra(palavraSecreta, chute, letrAcertada)
        else:
            erro += 1
        enforcou = (erro == 6)
        acertou = ('_' not in letrAcertada)
        print(letrAcertada)
    resultado(acertou, palavraSecreta)
    return

def jogaForca():
    print('Bem vindo ao Jogo da Forca.')
    loop(importaPalavra())
    return

if __name__ == "__main__":
    jogaForca()
