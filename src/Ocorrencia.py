from src.Funcionario import Funcionario


class Ocorrencia:
    def __init__(self, resumo: str, tipo: str, prioridade: str, responsavel: Funcionario):
        self.resumo = resumo
        self.tipo = tipo
        self.prioridade = prioridade

