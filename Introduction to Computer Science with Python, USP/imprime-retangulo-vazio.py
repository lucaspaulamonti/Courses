# Os caracteres que não estiverem na borda do retângulo devem ser espaçados.
largura=int(input('Digite a largura da área: '))
altura=int(input('Digite a altura da área: '))
print(largura*'#')
while(altura>2):
    print('#'+(largura-2)*' '+'#')
    altura=altura-1
print(largura*'#')