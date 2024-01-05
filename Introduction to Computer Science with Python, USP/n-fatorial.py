# Faça um programa em Python que receba um número natural n na entrada e imprima n! (fatorial) na saída.
n=int(input("Digite um número: "))
multiplo=1
resultado=1
while multiplo<=n:
    resultado=(resultado*multiplo)
    multiplo=multiplo+1
print(resultado)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!