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
    
    def adicionar_ocorrencia(self, resumo: str, tipo: str, prioridade: str, responsavel: Funcionario):
        self.verificar_colaborador_projeto(responsavel)
        ocorrencia = Ocorrencia(resumo, tipo, prioridade, responsavel)
        self.ocorrencias.append(ocorrencia)
        return ocorrencia.id

    def mudar_responsavel_ocorrencia(self, id: int, novo_responsavel: Funcionario):
        self.verificar_colaborador_projeto(novo_responsavel)
        ocorrencia_valida = None
        for ocorrencia in self.ocorrencias:
            if ocorrencia.id == id and ocorrencia.verificar_estado() == "aberta":
                ocorrencia_valida = ocorrencia
        if ocorrencia_valida is None:
            raise ValueError()
        ocorrencia_valida.mudar_responsavel(novo_responsavel)
        
    def fechar_ocorrencia(self, id: int):
        ocorrencia_final = None
        for ocorrencia in self.ocorrencias:
            if ocorrencia.id == id:
                ocorrencia_final = ocorrencia
        if ocorrencia_final is None:
            raise ValueError()
        ocorrencia_final.fechar_ocorrencia()
