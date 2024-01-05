# Faça um programa em Python que identifica se um número é divisível por 3 e por 5.
def fizzbuzz(numero):
    if (numero%3 == 0) and (numero%5 != 0):
        return 'Fizz'
    if (numero%3 != 0) and (numero%5 == 0):
        return 'Buzz'
    if (numero%3 == 0) and (numero%5 == 0):
        return 'FizzBuzz'
    if (numero%3 != 0) and (numero%5 != 0):
        return numero
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!