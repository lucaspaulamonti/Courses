# Faça um programa em Python que receba um número inteiro positivo na entrada e imprima os primeiros números ímpares naturais.
numero=int(input("Digite um número inteiro:"))
contador=0
resultado=0
impar=0
while numero>contador:
    resultado=impar%2
    if resultado!=0:
        print(impar)
        contador=contador+1
        impar=impar+1
    else:
        contador=contador
        impar=impar+1
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!