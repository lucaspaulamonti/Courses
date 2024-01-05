# Faça um programa em python que identifica números pares e ímpares.
terminou = False
p = i = 0
while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1
print ("P = ", p)
print ("I = ", i)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!