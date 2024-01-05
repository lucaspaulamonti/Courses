# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentualde desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.
preco_do_produto=float(input('Informe o preço do produto: '))
percentual_de_desconto=float(input('Informe o percetual de desconto (0-100)%: '))
desconto_do_produto=preco_do_produto*(percentual_de_desconto/100)
preco_final_do_produto=preco_do_produto-desconto_do_produto
print('O preço do produto é: R${}, o desconto é {}%.'.format(preco_do_produto,percentual_de_desconto))
print('Valor de desconto é: R${}. O valor final do produto é R${}.'.format(desconto_do_produto,preco_final_do_produto))
