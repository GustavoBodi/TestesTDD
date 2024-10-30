import unittest
from src.Funcionario import Funcionario
from src.Empresa import Empresa
from src.Projeto import Projeto


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

    def teste_adicionar_projeto_na_empresa_valido(self):
        nome = "Planta"
        orçamento = 2000
        projeto = Projeto(nome, orçamento)

        self.empresa.adicionar_projeto(projeto)

        assert self.empresa.projetos[0].nome == "Planta"
        assert self.empresa.projetos[0].orçamento == 2000
        assert self.empresa.projetos[0].colaboradores == []

    def teste_adicionar_projeto_na_empresa_duplicado(self):
        nome = "Planta"
        orçamento = 2000
        projeto_planta = Projeto(nome, orçamento)
        projeto_clone = Projeto(nome, orçamento)

        self.empresa.adicionar_projeto(projeto_planta)
        with self.assertRaises(ValueError):
            self.empresa.adicionar_projeto(projeto_clone)

    def teste_adicionar_projeto_com_funcionario_externo_erro(self):
        nome = "Planta"
        orçamento = 2000
        roberto = Funcionario("Roberto", "cpf", 1300, "chefe")
        self.empresa.adicionar_funcionario(roberto)
        projeto_planta = Projeto(nome, orçamento)
        robertao = Funcionario("Robertão", "cpfss", 1300, "chefe")
        projeto_planta.adicionar_colaborador(robertao)

        with self.assertRaises(ValueError):
            self.empresa.adicionar_projeto(projeto_planta)

    def teste_adicionar_funcionario_roberto_ao_projeto_planta_do_banco(self):
        nome = "Planta"
        orçamento = 2000
        roberto = Funcionario("Roberto", "cpf", 1300, "chefe")
        self.empresa.adicionar_funcionario(roberto)
        projeto_planta = Projeto(nome, orçamento)
        projeto_planta.adicionar_colaborador(roberto)

        self.empresa.adicionar_projeto(projeto_planta)

        assert self.empresa.projetos[0].colaboradores[0].cpf == "cpf"
        assert self.empresa.projetos[0].colaboradores[0].nome == "Roberto"
        assert self.empresa.projetos[0].colaboradores[0].salário == 1300
        assert self.empresa.projetos[0].colaboradores[0].cargo == "chefe"
        assert len(self.empresa.projetos[0].colaboradores) == 1
        assert len(self.empresa.projetos) == 1

    def teste_adicionar_multiplos_funcionarios_empresa(self):
        roberto = Funcionario("Roberto", "cpf", 1300, "chefe")
        robertao = Funcionario("Robertão", "cpfss", 1300, "chefe")
        self.empresa.adicionar_funcionario(roberto)
        self.empresa.adicionar_funcionario(robertao)
        len(self.empresa.funcionarios) == 2

    def teste_adicionar_multiplos_projetos_empresa(self):
        projeto_planta = Projeto("Planta", 2000)
        projeto_muda = Projeto("Muda", 3000)
        self.empresa.adicionar_projeto(projeto_planta)
        self.empresa.adicionar_projeto(projeto_muda)
        assert len(self.empresa.projetos) == 2

