import unittest
from src.Projeto import Projeto
from src.Funcionario import Funcionario


class ProjetoTest(unittest.TestCase):
    def teste_construtor_projeto_planta(self):
        nome = "Planta"
        orçamento = 2000

        projeto = Projeto(nome, orçamento)

        assert projeto.nome == nome
        assert projeto.orçamento == orçamento
        assert projeto.colaboradores == []

    def teste_construtor_com_orçamento_zero(self):
        nome = "Planta"
        orçamento = 0

        with self.assertRaises(ValueError):
            projeto = Projeto(nome, orçamento)

    def teste_adicionar_colaborador_no_projeto(self):
        nome = "Planta"
        orçamento = 2000
        projeto = Projeto(nome, orçamento)
        funcionario = Funcionario("Carlos", "cpf", 100, "chefe")
        projeto.adicionar_colaborador(funcionario)
        assert projeto.colaboradores[0].nome == "Carlos"
        assert projeto.colaboradores[0].cpf == "cpf"
        assert projeto.colaboradores[0].salário == 100
        assert projeto.colaboradores[0].cargo == "chefe"
