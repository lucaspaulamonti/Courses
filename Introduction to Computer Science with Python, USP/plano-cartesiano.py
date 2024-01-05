# Faça um programa em Python que calcule a distância para dois pontos num plano cartesiano.
xl=int(input())
yl=int(input())
xll=int(input())
yll=int(input())
d=((xl-xll)**2+(yl-yll)**2)**0.5
if d>=10:
    print('longe')
else:
    print('perto')
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso! 