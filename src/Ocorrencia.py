from src.Funcionario import Funcionario
import random


class Ocorrencia:
    def __init__(self, resumo: str, tipo: str, prioridade: str, responsavel: Funcionario):
        self.resumo = resumo
        self.tipo = tipo
        self.prioridade = prioridade
        if tipo not in ["tarefa", "bug", "melhoria"]:
            raise ValueError()
        if prioridade not in ["alta", "media", "baixa"]:
            raise ValueError()
        if responsavel.quantidade_ocorrencias == 10:
            raise ValueError()
        self.responsavel = responsavel
        self.responsavel.quantidade_ocorrencias += 1
        self.id = random.randint(1, 10000)

    def mudar_responsavel(self, novo_responsavel: Funcionario):
        self.responsavel.quantidade_ocorrencias -= 1
        novo_responsavel.quantidade_ocorrencias += 1
        self.responsavel = novo_responsavel
