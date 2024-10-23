import unittest
from src.Funcionario import Funcionario


class FuncionarioTest(unittest.TestCase):
    def teste_construtor_funcionario(self):
        nome = "Chefe"
        cpf = "cpf"
        salário = 1000
        cargo = "Chefe"

        funcionario = Funcionario(nome, cpf, salário, cargo)

        assert funcionario.nome == nome
        assert funcionario.cpf == cpf
        assert funcionario.salário == salário
        assert funcionario.cargo == cargo
