class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._like = 0

    def get_nome(self):
        return self._nome

    def get_ano(self):
        return self._ano

    def set_nome(self, nome):
        self._nome = nome

    def set_ano(self, ano):
        self._ano = ano

    def like(self):
        self._like += 1

class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def mostrarInfos(self):
        print(f'Nome do filme: {self._nome.title()}, ele foi feito em {self._ano} e tem a duração de {self.__duracao} e tem {self._like} likes')



class Serie(Programa):

    def __init__(self, nome, ano,  temporada):
        super().__init__(nome, ano)
        self.__temporada = temporada


    def get_temporada(self):
        return self.__temporada

    def set_temporada(self, temporada):
        self.__temporada = temporada

    def mostrarInfos(self):
        print(f'Nome da serie: {self._nome.title()}, ele foi feito em {self._ano} e falamos da temporada {self.__temporada} e tem {self._like} likes')
1

filme = Filme("vingadores", 2010, "2 horas")
filme.mostrarInfos()
filme.like()
filme.mostrarInfos()

serie = Serie("La Casa de Papel", 2017, "temporada 1")
serie.set_temporada("Temporada 2")
serie.mostrarInfos()
serie.like()
serie.mostrarInfos()