# Faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos.
entradasegundos=int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias=entradasegundos//86400
horas=entradasegundos%86400//3600
minutos=entradasegundos%3600//60
segundos=entradasegundos%60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!