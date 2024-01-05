# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
def vogal(a):
    vogal=True
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
        vogal=True
    else:
        vogal=False
    return vogal
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!