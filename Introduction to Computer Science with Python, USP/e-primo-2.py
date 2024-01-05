# Faça um programa em Python que identifique se um número é primo.
numero=int(input("Digite um número inteiro: "))
contador=2
sobra= 0
naoprimo=False
while contador<numero:
	sobra=numero%contador
	contador=contador+1
	if sobra==0:
		naoprimo=True
if naoprimo or numero==1:
	print("nao primo")
else:
	print("primo")
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!