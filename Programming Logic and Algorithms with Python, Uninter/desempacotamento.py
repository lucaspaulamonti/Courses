# Crie uma função que some quantos números forem necessários.
def soma(*num):
    soma=int()
    print('Tupla: {}'.format(num))
    for(i)in(num):
        soma+=i
    return soma
print('Resultado: {}\n'.format(soma(1,2,3)))
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))