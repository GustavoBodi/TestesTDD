import unittest


class Funcionario(unittest.TestCase):
    def __init__(self, nome: str, cpf: str, salário: int, cargo: str):
        if nome is None or cpf is None or salário is None or cargo is None:
            raise ValueError()
        self.nome = nome
        self.cpf = cpf
        self.salário = salário
        self.cargo = cargo
        self.quantidade_ocorrencias = 0
