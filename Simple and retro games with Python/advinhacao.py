import random


def jogaAdvinhacao():
    print('Bem vindo ao Jogo de Advinhação.')
    numeroSecreto = random.randrange(1, 101)
    ponto = 1000

    nivel = int(input('Qual o nível de dificuldade?\n[1] Fácil, [2] Médio ou [3] Difícil?\n> '))

    if nivel == 1:
        totalTentativa = 20
    elif nivel == 2:
        totalTentativa = 10
    else:
        totalTentativa = 5

    for rodada in range(1, totalTentativa + 1):
        print('Tentativa {}/{}.'.format(rodada, totalTentativa))
        chute = int(input('Informe um número entre 1 (um) e 100 (cem).\n> '))

        if chute == numeroSecreto:
            print('Você acertou!\nFez {} pontos.'.format(ponto))
            break
        else:
            if chute > numeroSecreto:
                print('Você errou! O seu chute foi maior > que o número secreto.')
            else:
                print('Você errou! O seu chute foi menor < que o número secreto.')
            ponto = ponto - (abs(numeroSecreto - chute))

    print('Fim de Jogo.')
    return


if __name__ == "__main__":
    jogaAdvinhacao()
