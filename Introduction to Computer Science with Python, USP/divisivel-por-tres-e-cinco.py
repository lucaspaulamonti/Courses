# Faça um programa em Python que identifica se um número é divisível por 3 e por 5.
numero=(int(input("Insira um número inteiro: ")))
if (numero%3 == 0) and (numero%5 == 0):
    print("FizzBuzz")
else:
    print(numero)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!