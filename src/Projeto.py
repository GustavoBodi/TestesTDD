from src.Funcionario import Funcionario


class Projeto:
    def __init__(self, nome: str, orçamento: int):
        if orçamento <= 0:
            raise ValueError()
        self.nome = nome
        self.orçamento = orçamento
        self.colaboradores = []

    def adicionar_colaborador(self, colaborador: Funcionario):
        for colaborador_lista in self.colaboradores:
            if colaborador.cpf == colaborador_lista.cpf:
                return
        self.colaboradores.append(colaborador)
