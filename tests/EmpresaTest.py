import unittest
from src.Funcionario import Funcionario
from src.Empresa import Empresa


class EmpresaTest(unittest.TestCase):
    def setUp(self):
        nome_empresa = "Banco"
        empresa = Empresa(nome_empresa)
        self.empresa = empresa

    def teste_criar_empresa_banco(self):
        nome_empresa = "Banco"
        empresa = Empresa(nome_empresa)
        assert empresa.funcionarios == []
        assert empresa.projetos == []
        assert empresa.nome == nome_empresa

    def teste_criar_empresa_nome_vazio(self):
        nome_empresa = ""
        with self.assertRaises(Exception):
            self.empresa = Empresa(nome_empresa)

    def teste_adicionar_funcionario_roberto_no_banco(self):
        funcionario = Funcionario("roberto", "cpf", 1000, "chefe")

        self.empresa.adicionar_funcionario(funcionario)

        assert self.empresa.funcionarios[0].nome == "roberto"
        assert self.empresa.funcionarios[0].cpf == "cpf"
        assert self.empresa.funcionarios[0].salário == 1000
        assert self.empresa.funcionarios[0].cargo == "chefe"

    def teste_adicionar_funcionario_duplicado_no_banco(self):
        funcionario = Funcionario("roberto", "cpf", 1000, "chefe")
        self.empresa.adicionar_funcionario(funcionario)
        with self.assertRaises(ValueError):
            self.empresa.adicionar_funcionario(funcionario)

    def teste_adicionar_funcionario_cpf_duplicado_no_banco(self):
        roberto = Funcionario("roberto", "cpf", 1000, "chefe")
        jeffersson = Funcionario("jeffersson", "cpf", 1000, "chefe")
        self.empresa.adicionar_funcionario(roberto)
        with self.assertRaises(ValueError):
            self.empresa.adicionar_funcionario(jeffersson)



