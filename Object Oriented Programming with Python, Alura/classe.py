class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__like = 0

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, a):
        self.__nome = a.title()

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, a):
        self.__ano = a

    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self, a):
        self.__duracao = a

    @property
    def like(self):
        return self.__like
    @like.setter
    def like(self, a):
        self.__like = a


    def darLike(self):
        self.__like += 1


class Serie:
    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporada = temporada
        self.__like = 0

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, a):
        self.__nome = a.title()

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, a):
        self.__ano = a

    @property
    def temporada(self):
        return self.__temporada
    @temporada.setter
    def temporada(self, a):
        self.temporada = a

    @property
    def like(self):
        return self.__like
    @like.setter
    def like(self, a):
        self.__like = a


    def darLike(self):
        self.__like += 1

starwars = Filme('Star Wars: Episode VI – Return of the Jedi',1983,160)
bojack = Serie('BoJack Horseman',2014,6)

