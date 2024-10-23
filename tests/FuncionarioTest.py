import unittest


class FuncionarioTest(unittest.TestCase):
    def teste_construtor_funcionario(self):
        nome = "Chefe"
        cpf = "cpf"
        salário = 1000
        cargo = "Chefe"

        funcionario = Funcionario(nome, cpf, numero_de_telefone, endereço, salário)

        assert funcionario.nome == nome
        assert funcionario.cpf == cpf
        assert funcionario.salário == salário
        assert funcionario.cargo == cargo
