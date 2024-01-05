# Crie uma lista de compras que tenha várias listas dentro.
item=[]
compras=[]
for(i)in(range(3)):
    item.append(input('Informe o nome: '))
    item.append(int(input('Informe a quantidade: ')))
    item.append(float(input('Informe o custo: ')))
    compras.append(item[:])
    item.clear()
print(compras)
