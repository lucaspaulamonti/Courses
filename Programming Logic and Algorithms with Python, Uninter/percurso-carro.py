# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado, assim como a quantidade de dias. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
qnt_km=int(input('Informe quantos kms foram percorridos: '))
qnt_dias=int(input('Informe por quantos dias foi alugado: '))
result=(60*qnt_dias)+(0.15*qnt_km)
print('KM: {}.'.format(qnt_km))
print('Dias: {}.'.format(qnt_dias))
print('A pagar: R${}.'.format(result))