
class Projeto:
    def __init__(self, nome: str, orçamento: int):
        if orçamento == 0:
            raise ValueError()
        self.nome = nome
        self.orçamento = orçamento
        self.colaboradores = []
