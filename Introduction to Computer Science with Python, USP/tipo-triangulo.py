# Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que devolve uma string dizendo se o triângulo é: isósceles, equilátero ou escaleno.
if(__name__)=='__main__':
    class Triangulo():
        def __init__(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c
        def perimetro(self):
            self.perim=((self.a)+(self.b)+(self.c))
            return self.perim
        def semelhantes(self,triangulo):
            triangulo_1=[self.a,self.b,self.c]
            triangulo_2=[triangulo.a,triangulo.b,triangulo.c]
            sorted(triangulo_1)
            sorted(triangulo_2)
            if triangulo_1[0]/triangulo_2[0]==triangulo_1[1]/triangulo_2[1]==triangulo_1[2]/triangulo_2[2]:
                return True
            else:
                return not True
        def tipo_lado(self):
            tipo_lado=['isósceles','equilátero','escaleno']
            if((self.a)==(self.b))and((self.a)==(self.c)):
                return tipo_lado[1]
            elif((self.a)!=(self.b))and((self.a)!=(self.c)):
                return tipo_lado[2]
            else:
                return tipo_lado[0]
        pass
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!