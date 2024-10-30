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

    def teste_adicionar_colaborador_duplicado_no_projeto(self):
        nome = "Planta"
        orçamento = 2000
        projeto = Projeto(nome, orçamento)
        funcionario = Funcionario("Carlos", "cpf", 100, "chefe")
        projeto.adicionar_colaborador(funcionario)
        projeto.adicionar_colaborador(funcionario)
        assert projeto.colaboradores[0].nome == "Carlos"
        assert projeto.colaboradores[0].cpf == "cpf"
        assert projeto.colaboradores[0].salário == 100
        assert projeto.colaboradores[0].cargo == "chefe"
        assert len(projeto.colaboradores) == 1

    def teste_criar_ocorrencia_projeto(self):
        nome = "Planta"
        orçamento = 2000
        projeto = Projeto(nome, orçamento)
        funcionario = Funcionario("Carlos", "cpf", 100, "chefe")
        projeto.adicionar_colaborador(funcionario)
        tipo = "tarefa"
        prioridade = "baixa"
        resumo = "resumo"
        projeto.adicionar_ocorrencia(resumo, tipo, prioridade, funcionario)

    def teste_criar_ocorrencia_funcionario_outro_projeto_falha(self):
        nome = "Planta"
        orçamento = 2000
        projeto = Projeto(nome, orçamento)
        funcionario = Funcionario("Carlos", "cpf", 100, "chefe")
        tipo = "tarefa"
        prioridade = "baixa"
        resumo = "resumo"
        with self.assertRaises(ValueError):
            projeto.adicionar_ocorrencia(resumo, tipo, prioridade, funcionario)

    def teste_adicionar_multiplos_funcionarios_projeto(self):
        projeto_planta = Projeto("Planta", 5000)
        carlos = Funcionario("Carlos", "cpf", 100, "chefe")
        jefersson = Funcionario("Jefersson", "cpff", 100, "chefe")
        projeto_planta.adicionar_colaborador(carlos)
        projeto_planta.adicionar_colaborador(jefersson)
        assert len(projeto_planta.colaboradores) == 2

    def teste_mudar_responsavel_ocorrencia(self):
        nome = "Planta"
        orçamento = 2000
        projeto = Projeto(nome, orçamento)
        responsavel = Funcionario("Carlos", "cpf", 100, "chefe")
        novo_responsavel = Funcionario("Carlos", "cpf", 100, "chefe")
        projeto.adicionar_colaborador(responsavel)
        tipo = "tarefa"
        prioridade = "baixa"
        resumo = "resumo"
        id = projeto.adicionar_ocorrencia(resumo, tipo, prioridade, responsavel)

        projeto.mudar_responsavel_ocorrencia(id, novo_responsavel)

        assert projeto.ocorrencias[0].responsavel.cpf == novo_responsavel.cpf

    def teste_mudar_responsavel_ocorrencia_inexistente(self):
        projeto = Projeto("Planta", 3000)
        responsavel = Funcionario("Carlos", "cpf", 100, "chefe")
        novo_responsavel = Funcionario("Carl~ao", "cpff", 100, "chefe")
        projeto.adicionar_colaborador(responsavel)
        projeto.adicionar_colaborador(novo_responsavel)
        projeto.adicionar_ocorrencia("resumo", "tarefa", "baixa", responsavel)
        with self.assertRaises(ValueError):
            projeto.mudar_responsavel_ocorrencia(-1, novo_responsavel)

