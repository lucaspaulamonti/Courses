# Escreva um programa em python que indica se tal número é primo ou não.
def eprimo(n):
    fator=2
    if(n==2):
        return True
    while(n%fator!=0)and(fator<=n/2):
        fator=fator+1
    if(n%fator==0):
        return False
    else: 
        return True
n=int(input('Digite um número inteiro: '))
while(n>0):
    if(eprimo(n)):
        print(n,'é primo.')
    else:
        print(n,'não é primo.')
    n=int(input('Digite um número inteiro: '))
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!