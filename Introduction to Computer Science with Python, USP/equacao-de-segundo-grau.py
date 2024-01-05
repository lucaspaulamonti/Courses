# Escreva um programa em Python que calcula as raízes de uma equação do segundo grau.
import math
a=float(input('Digite o valor de A: '))
b=float(input('Digite o valor de B: '))
c=float(input('Digite o valor de C: '))
delta=b**2-4*a*c
if delta==0:
    raiz1=(-b+math.sqrt(delta))/(2*a)
    print('A única raiz é:',raiz1)
else:
    if delta<0:
        print('Esta equação não possúi raízes reais.')
    else:
        raiz1=(-b+math.sqrt(delta))/(2*a)
        raiz2=(-b-math.sqrt(delta))/(2*a)
        print('A primeira raiz é:',raiz1)
        print('A segunda raiz é:',raiz2)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso! 