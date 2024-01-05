# Crie uma docstring para a função soma.
def som(x=0,y=0,z=0):
    '''Retorna o somatório de até 3 (três) valores numéricos quaisquer.
    Todos os parâmetros são opcionais (0).
    
    x: Valor Numérico (opcional: (0));
    y: Valor Numérico (opcional: (0));
    z: Valor Numérico (opcional: (0)).'''
    return x+y+z
print(som(3,2))
help(som)