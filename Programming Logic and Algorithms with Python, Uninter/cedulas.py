# Informe um valor e retorne quantas cédulas de cada tipo são necessárias para totalizar o valor.
rs=int(input('Informe o valor em R$: '))
while(True):
    if(rs>=100):
        v100=rs//100
        rs-=v100*100
        print('Cédulas de R$100,00:',v100)
        if(not rs):
            break
    if(rs>=50):
        v50=rs//50
        rs-=v50*50
        print('Cédulas de R$50,00:',v50)
        if(not rs):
            break
    if(rs>=20):
        v20=rs//20
        rs-=v20*20
        print('Cédulas de R$20,00:',v20)
        if(not rs):
            break
    if(rs>=10):
        v10=rs//10
        rs-=v10*10
        print('Cédulas de R$10,00:',v10)
        if(not rs):
            break
    if(rs>=5):
        v5=rs//5
        rs-=v5*5
        print('Cédulas de R$5,00:',v5)
        if(not rs):
            break
    if(rs):
        v1=rs
        print('Cédulas de R$1,00:',v1)
        break