# Crie uma função que calcula o fatorial de n, valide n por meio de outra função e possua help.
def valida(q,min,max):
    x=int(input(q))
    while(((x)<(min))or((x)>(max))):
        x=int(input(q))
    return x
def fatorial(n):
    '''Calcula o fatorial.'''
    fat=1
    if(n==0):
        return fat
    for(i)in(range(1,n+1)):
        fat*=i
    return fat