import unittest
from src.Funcionario import Funcionario
from src.Empresa import Empresa
from src.Projeto import Projeto


class OcorrenciaTest(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario("robertao", "cpf", 1200, "chefe")

    def teste_criar_ocorrencia_sucesso(self):
        resumo = "Resumo"
        tipo = "tarefa"
        prioridade = "media"
        ocorrencia = Ocorrencia(resumo, tipo, prioridade, self.funcionario)
        assert ocorrencia.resumo == resumo
        assert ocorrencia.tipo == tipo
        assert ocorrencia.funcionario.cpf == self.funcionario.cpf

