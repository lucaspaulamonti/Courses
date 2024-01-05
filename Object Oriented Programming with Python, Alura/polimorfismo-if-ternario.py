class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, a):
        self._nome = a.title()

    @property
    def ano(self):
        return self._ano
    @ano.setter
    def ano(self, a):
        self._ano = a

    @property
    def like(self):
        return self._like
    @like.setter
    def like(self, a):
        self._like = a


    def darLike(self):
        self._like += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada


starwars = Filme('Star Wars: Episode VI – Return of the Jedi',1983,160)
bojack = Serie('BoJack Horseman',2014,6)

lista = [starwars, bojack]

for programa in lista:
    detalhe = programa._duracao if hasattr(programa, '_duracao') else programa._temporada
    print(programa.nome)
    print(detalhe)
    print(programa.ano)
    print(programa.like)