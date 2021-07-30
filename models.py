class Filme:
    def __init__(self, nome_filme, ano, classificacao, duracao, genero, diretor, elenco, resumo, poster, id=None):
        self.id = id
        self.nome_filme = nome_filme
        self.ano = ano
        self.classificacao = classificacao
        self.duracao = duracao
        self.genero = genero
        self.diretor = diretor
        self.elenco = elenco
        self.resumo = resumo
        self.poster = poster