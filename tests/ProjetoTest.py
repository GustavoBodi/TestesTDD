import unittest
from src.Projeto import Projeto


class ProjetoTest(unittest.TestCase):
    def teste_construtor_projeto_planta(self):
        nome = "Planta"
        orçamento = 2000

        projeto = Projeto(nome, orçamento)

        assert projeto.nome == nome
        assert projeto.orçamento == orçamento
        assert projeto.colaboradores == []

    def teste_orçamento_zero(self):
        nome = "Planta"
        orçamento = 0

        with self.assertRaises(ValueError):
            projeto = Projeto(nome, orçamento)

