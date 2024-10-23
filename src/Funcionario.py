import unittest


class Funcionario(unittest.TestCase):
    def __init__(self, nome: str, cpf: str, salário: int, cargo: str):
        self.nome = nome
        self.cpf = cpf
        self.salário = salário
        self.cargo = cargo
