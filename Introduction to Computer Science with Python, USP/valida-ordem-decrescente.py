# Faça um programa em python que valide se uma sequência está em ordem decrescente.
decrescente=True
anterior=int(input("Digite o primeiro número da sequência: "))
valor=1
while valor!=0 and decrescente:
    valor =int(input("Digite o próximo número da sequência: "))
    if valor>anterior:
        decrescente=False
    anterior=valor
if decrescente:
    print("A sequência está em ordem decrescente.")
else:
    print("A sequência NÃO está em ordem decrescente.")
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!