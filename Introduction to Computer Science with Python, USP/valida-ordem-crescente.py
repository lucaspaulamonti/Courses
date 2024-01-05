# Faça um programa em python que valide se uma sequência está em ordem crescente.
crescente=True
anterior=int(input("Digite o primeiro número da sequência: "))
valor=1
while valor<10 and crescente:
    valor=int(input("Digite o próximo número da sequência: "))
    if valor<anterior:
        crescente=False
    anterior=valor
if crescente:
    print("A sequência está em ordem crescente.")
else:
    print("A sequência NÃO está em ordem crescente.")
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!