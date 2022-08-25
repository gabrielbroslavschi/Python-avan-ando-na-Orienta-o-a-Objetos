class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._like = 0
    @property
    def nome(self):
        return self._nome
    @property
    def ano(self):
        return self._ano

    def set_nome(self, nome):
        self._nome = nome.title()

    def set_ano(self, ano):
        self._ano = ano

    def like(self):
        self._like += 1

    @property
    def glike(self):
        return self._like

    def __str__(self):
         return f'{self._nome} - {self.ano} - {self.glike} likes'

class Filme (Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def mostrarInfos(self):
        print(f'Nome do filme: {self._nome.title()}, ele foi feito em {self._ano} e tem a duração de {self.__duracao} e tem {self._like} likes')

    def __str__(self):
        return f'{self._nome} - {self.duracao} -  {self.ano} - {self.glike} likes'

class Serie(Programa):

    def __init__(self, nome, ano,  temporada):
        super().__init__(nome, ano)
        self.__temporada = temporada
        
    @property
    def temporada(self):
        return self.__temporada

    def set_temporada(self, temporada):
        self.__temporada = temporada

    def mostrarInfos(self):
        print(f'Nome da serie: {self._nome.title()}, ele foi feito em {self._ano} e falamos da temporada {self.__temporada} e tem {self._like} likes')

    def __str__(self):
        return f'{self._nome} - {self.temporada} -  {self.ano} - {self.glike} likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]



filme1 = Filme("vingadores", 2010, "2 horas")
filme2 = Filme("Tropa de elite", 2008, "2horas")
filme3 = Filme("A espera de um milagre", 2001, "3horas")
serie1 = Serie("La Casa de Papel", 2017, "temporada 1")
serie2 = Serie("Stranger Thing", 2018, "temporada 4")
serie3 = Serie("Friends", 2001, "temporada 6")





filmes_e_series = [filme1, filme2, filme3, serie1, serie2, serie3]
playlist = Playlist('lista do fim de semana', filmes_e_series)

print(f'O tamanho da playlist : {len(playlist)}')

for programa in playlist:
    print(programa)





