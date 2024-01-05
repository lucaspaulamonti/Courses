# Crie uma exceção para tratar o erro ValueError.
while True:
    try:
        value=int(input('Informe um número: '))
        break
    except ValueError:
        print('Esperado um número inteiro.')