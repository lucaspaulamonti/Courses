# Aperfeiçoe o algorítmo de operação utilizando while.
while(True):
    x=float(input('Informe X: '))
    op=input('Informe a operação a ser realizada (+, -, * ou /): ')
    y=float(input('Informe Y: '))
    if(op=='+'):
        print('Total: {} + {} = {}.'.format(x,y,x+y))
        continue
    elif(op=='-'):
        print('Total: {} - {} = {}.'.format(x,y,x-y))
        continue
    elif(op=='*'):
        print('Total: {} * {} = {}.'.format(x,y,x*y))
        continue
    elif(op=='/'):
        print('Total: {} / {} = {}.'.format(x,y,x/y))
        continue
    elif(op=='s'):
        break
    else:
        print('Operação inválida.')
print('Encerrando o programa.')