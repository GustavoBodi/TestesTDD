import unittest
from src.Empresa import Empresa


class EmpresaTest(unittest.TestCase):
    def teste_criar_empresa_banco(self):
        nome_empresa = "Banco"
        empresa = Empresa(nome_empresa)
        assert empresa.funcionarios == []
        assert empresa.projetos == []
        assert empresa.nome == nome_empresa

    def teste_criar_empresa_nome_vazio(self):
        nome_empresa = ""
        with self.assertRaises(Exception):
            empresa = Empresa(nome_empresa)
