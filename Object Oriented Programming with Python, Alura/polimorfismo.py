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

    def __str__(self):
        return f'Nome: {self.nome} Ano: {self.ano} Likes: {self.like}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} Ano: {self.ano} Likes: {self.like} Duração: {self._duracao}'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada

    def __str__(self):
        return f'Nome: {self.nome} Ano: {self.ano} Likes: {self.like} Temporadas: {self._temporada}'

class Playlist:
    def __init__(self, nome, programa):
        self._nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    def __len__(self):
        return len(self._programa)

    @property
    def list(self):
        return self._programa


starwars = Filme('Star Wars: Episode VI – Return of the Jedi', 1983, 160)
bojack = Serie('BoJack Horseman', 2014, 6)
tenaciousd = Filme('Tenacious D in: The Pick of Destiny', 2006, 160)
breakingbad = Serie('Breaking Bad', 2008, 5)
lista = [starwars, bojack, tenaciousd, breakingbad]

playlist = Playlist('MinhaPlaylist', lista)

for programa in playlist:
    print(programa)


