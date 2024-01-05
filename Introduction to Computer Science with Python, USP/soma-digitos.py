# Faça um programa em python que some os dígitos de um número informado.
numero=int(input("Digite o número:"))
resultado=1
soma=0
while numero!=0:
    resultado=numero%10
    numero=numero//10
    soma=soma+resultado
print(soma)
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!