# Crie uma função que adapte uma borda para uma palavra, destacando-a.
def borda(s1):
    if len(s1):
        print('+','-'*len(s1),'-','+')
        print('| ',s1,' |')
        print('+','-'*len(s1),'-','+')
s1=input('Informe uma palavra a ser realçada: ')
borda(s1)
