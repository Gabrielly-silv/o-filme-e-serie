class Programa:
    def __init__(self, nome, Ano):
        self._nome = nome.title()
        self.Ano = Ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome
   
    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self._likes} likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        self._likes = 0

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        self._likes = 0

class playlist(list):
    def __init__(self,nome,programas):
        self.nome = nome 
        super().__init__(programas)


vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2 )

vingadores.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = playlist ('fim de semana', filmes_e_series)

print (f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana: 
    print (programa)

print(f'Está ou não está? {demolidor in playlist_fim_de_semana}') 

