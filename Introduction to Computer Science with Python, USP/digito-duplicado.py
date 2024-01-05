# Faça um programa em Python que valide se um número possúi um mesmo caracter seguido.
numero=int(input("Digite um número inteiro:"))
loop=True
resultadoatual=0
resultadoanterior='n'
while loop:
    resultadoatual=int(numero%10)
    numero=numero//10
    if resultadoatual == resultadoanterior:
        print("sim")
        loop=False
    else:
        resultadoanterior=int(resultadoatual)
        resultadoatual=str('x')
        loop=True
        if numero==0:
            print("não")
            loop=False
        else:
            loop=True
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!