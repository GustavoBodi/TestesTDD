from src.Funcionario import Funcionario
from src.Ocorrencia import Ocorrencia


class Projeto:
    def __init__(self, nome: str, orçamento: int):
        if orçamento <= 0:
            raise ValueError()
        self.nome = nome
        self.orçamento = orçamento
        self.colaboradores = []
        self.ocorrencias = []

    def adicionar_colaborador(self, colaborador: Funcionario):
        for colaborador_lista in self.colaboradores:
            if colaborador.cpf == colaborador_lista.cpf:
                return
        self.colaboradores.append(colaborador)

    def verificar_colaborador_projeto(self, colaborador: Funcionario):
        for colaborador_lista in self.colaboradores:
            if colaborador.cpf == colaborador_lista.cpf:
                return
        raise ValueError()

    def adicionar_ocorrencia(self, resumo: str, tipo: str, prioridade: str, funcionario: Funcionario):
        self.verificar_colaborador_projeto(funcionario)
        ocorrencia = Ocorrencia(resumo, tipo, prioridade, funcionario)
        self.ocorrencias.append(ocorrencia)
