# Crie uma variável de string que recebe uma frase qualquer. Crie uma segunda variável agora contendo metade da string digitada. Imprima somente os dois últimos caracteres da segunda variável.
frase_completa=input('Digite uma frase: ')
frase_metade=frase_completa[:int(len(frase_completa)/2)]
print(frase_metade[-2:])