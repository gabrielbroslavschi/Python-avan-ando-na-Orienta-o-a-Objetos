class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    def get_nome(self):
        return self.__nome

    def get_ano(self):
        return self.__ano

    def get_duracao(self):
        return self.__duracao

    def set_nome(self, nome):
        self.__nome = nome

    def set_ano(self, ano):
        self.__ano = ano

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def mostrarInfos(self):
        print(f'Nome do filme: {self.__nome.title()}, ele foi feito em {self.__ano} e tem a duração de {self.__duracao} e tem {self.__likes} likes')

    def like(self):
        self.__likes += 1


class Serie:

    def __init__(self, nome, ano, temporada):
        self.__nome = nome
        self.__ano = ano
        self.__temporada = temporada
        self.__likes = 0

    def get_nome(self):
        return self.__nome

    def get_ano(self):
        return self.__ano

    def get_temporada(self):
        return self.__temporada

    def set_nome(self, nome):
        self.__nome = nome

    def set_ano(self, ano):
        self.__ano = ano

    def set_temporada(self, temporada):
        self.__temporada = temporada

    def mostrarInfos(self):
        print(f'Nome da serie: {self.__nome.title()}, ele foi feito em {self.__ano} e falamos da temporada {self.__temporada} e tem {self.__likes} likes')

    def like(self):
        self.__likes += 1

filme = Filme("vingadores", 2010, "2 horas")
filme.mostrarInfos()
filme.like()
filme.mostrarInfos()

serie = Serie("La Casa de Papel", 2017, "temporada 1")
serie.set_temporada("Temporada 2")
serie.mostrarInfos()
serie.like()
serie.mostrarInfos()