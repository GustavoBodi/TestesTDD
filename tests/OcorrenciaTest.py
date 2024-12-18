import unittest
from src.Funcionario import Funcionario
from src.Empresa import Empresa
from src.Projeto import Projeto
from src.Ocorrencia import Ocorrencia


class OcorrenciaTest(unittest.TestCase):
    def setUp(self):
        self.responsavel = Funcionario("robertao", "cpf", 1200, "chefe")
        self.resumo = "resumo"

    def teste_criar_ocorrencia_sucesso(self):
        tipo = "tarefa"
        prioridade = "media"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.resumo == self.resumo
        assert ocorrencia.tipo == tipo
        assert ocorrencia.responsavel.cpf == self.responsavel.cpf

    def teste_criar_ocorrencia_tarefa(self):
        tipo = "tarefa"
        prioridade = "baixa"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.tipo == tipo

    def teste_criar_ocorrencia_melhoria(self):
        tipo = "melhoria"
        prioridade = "baixa"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.tipo == tipo

    def teste_criar_ocorrencia_bug(self):
        tipo = "bug"
        prioridade = "baixa"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.tipo == tipo

    def teste_criar_ocorrencia_inexistente(self):
        tipo = "aaa"
        prioridade = "baixa"
        with self.assertRaises(ValueError):
            Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)

    def teste_criar_prioridade_alta(self):
        tipo = "tarefa"
        prioridade = "alta"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.tipo == tipo

    def teste_criar_prioridade_media(self):
        tipo = "tarefa"
        prioridade = "media"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.tipo == tipo

    def teste_criar_prioridade_baixa(self):
        tipo = "tarefa"
        prioridade = "baixa"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.tipo == tipo

    def teste_criar_prioridade_inexistente(self):
        tipo = "tarefa"
        prioridade = "aaa"
        with self.assertRaises(ValueError):
            Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)

    def teste_criar_identificador_diferente_ocorrencia(self):
        tipo = "tarefa"
        prioridade = "baixa"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        ocorrencia2 = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        assert ocorrencia.id != ocorrencia2.id

    def teste_modificar_responsavel(self):
        tipo = "tarefa"
        prioridade = "baixa"
        ocorrencia = Ocorrencia(self.resumo, tipo, prioridade, self.responsavel)
        responsavel_roberto = Funcionario("roberto", "cpf2", 1400, "chefe")

        ocorrencia.mudar_responsavel(responsavel_roberto)

        assert ocorrencia.responsavel.cpf == responsavel_roberto.cpf
        assert responsavel_roberto.quantidade_ocorrencias == 1
        assert self.responsavel.quantidade_ocorrencias == 0

    def teste_adicionar_onze_projetos_erro(self):
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        with self.assertRaises(ValueError):
            Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
            
    def teste_verificar_estado_inicial_aberta(self):
        ocorrencia = Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        
        assert ocorrencia.estado == "aberta"
        assert self.responsavel.quantidade_ocorrencias == 1
        
    def teste_fechar_ocorrencia_aberta(self):
        ocorrencia = Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        ocorrencia.fechar_ocorrencia()
        
        assert ocorrencia.estado == "fechada"
        assert self.responsavel.quantidade_ocorrencias == 0
    
    def teste_fechar_ocorrencia_fechada(self):
        ocorrencia = Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        ocorrencia.fechar_ocorrencia()
        
        with self.assertRaises(ValueError):
            ocorrencia.fechar_ocorrencia()

    def teste_alterar_prioridade_baixa_para_alta_aberta(self):
        ocorrencia = Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        nova_prioridade = "alta"
        ocorrencia.alterar_prioridade(nova_prioridade)
        
        assert ocorrencia.prioridade == "alta"
    
    def teste_alterar_prioridade_baixa_para_alta_fechada(self):
        ocorrencia = Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        ocorrencia.fechar_ocorrencia()
        nova_prioridade = "alta"

        with self.assertRaises(ValueError):
            ocorrencia.alterar_prioridade(nova_prioridade)
            
    def teste_alterar_prioridade_inexistente(self):
        ocorrencia = Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        nova_prioridade = "xxxxx"
        
        with self.assertRaises(ValueError):
            ocorrencia.alterar_prioridade(nova_prioridade)
    
    def teste_alterar_prioridade_baixa_para_baixa_falha(self):
        ocorrencia = Ocorrencia("resumo", "tarefa", "baixa", self.responsavel)
        nova_prioridade = "baixa"

        with self.assertRaises(ValueError):
            ocorrencia.alterar_prioridade(nova_prioridade)