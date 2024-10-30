from src.Funcionario import Funcionario


class Ocorrencia:
    def __init__(self, resumo: str, tipo: str, prioridade: str, responsavel: Funcionario):
        self.resumo = resumo
        self.tipo = tipo
        self.prioridade = prioridade
        if tipo not in ["tarefa", "bug", "melhoria"]:
            raise ValueError()
        if prioridade not in ["alta", "media", "baixa"]:
            raise ValueError()
        if responsavel.quantidade_projetos == 10:
            raise ValueError()
        self.responsavel = responsavel
        self.responsavel.quantidade_projetos += 1

