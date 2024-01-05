# Questão 1.
# Identificação.
def identificacao():
    lucasdepaulamonti_4170082='Lucas de Paula Monti'
    print('Seja bem-vindo a loja do {}.'.format(lucasdepaulamonti_4170082))

# calculoValores.
def calculoValores(valorUnitario,qnt,descAplicado=0):
    subtotal=valorUnitario*qnt
    total=subtotal-(subtotal*descAplicado)
    print('Valor SEM desconto foi R$: {:.2f}.'.format(subtotal))
    print('Valor COM desconto foi R$: {:.2f} (desc. de {}%).'.format(total,descAplicado*100))

# guiaValores.
def guiaValores(valorUnitario,qnt):
    if(qnt<5):# até 4un/ 0% desc.
        calculoValores(valorUnitario,qnt)
    elif(5<=qnt<20):# de 5un a 19un/ 3% desc.
        calculoValores(valorUnitario,qnt,0.03)
    elif(20<=qnt<100):# de 20un a 99un/ 6% desc.
        calculoValores(valorUnitario,qnt,0.06)
    else:# 100un ou mais/ 10% desc.
        calculoValores(valorUnitario,qnt,0.1)

# entradaInvalida.
def entradaInvalida():
    print('Os valores informados devem ser numéricos, positivos e caso sejam decimais, deve ser utilizado \'.\'. Ex: R$40.00.')

# Main.
identificacao()
while True:
    try:
        valorUnitario=float(input('Informe o valor unitário R$: '))
        qnt=float(input('Informe a quantidade: '))
        if(valorUnitario>=0)and(qnt>0):# posseguir se valor e quantidade não forem negativos.
            guiaValores(valorUnitario,qnt)
            break
        entradaInvalida()
    except:
        entradaInvalida()