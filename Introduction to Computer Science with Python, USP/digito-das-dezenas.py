# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
numero=int(input("Digite um número inteiro: "))
unidade=numero//10
dezena=unidade//10
print("O dígito das dezenas é",unidade%10)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!