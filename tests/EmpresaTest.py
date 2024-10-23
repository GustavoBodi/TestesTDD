import unittest
from src.Funcionario import Funcionario
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

    def teste_adicionar_funcionario_roberto_no_banco(self):
        nome_empresa = "Banco"
        empresa = Empresa(nome_empresa)
        funcionario = Funcionario("roberto", "cpf", 1000, "chefe")

        empresa.adicionar_funcionario(funcionario)

        assert empresa.funcionarios[0].nome == "roberto"
        assert empresa.funcionarios[0].cpf == "cpf"
        assert empresa.funcionarios[0].salário == 1000
        assert empresa.funcionarios[0].cargo == "chefe"
