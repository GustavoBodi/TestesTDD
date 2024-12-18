from src.Funcionario import Funcionario
from src.Projeto import Projeto
from src.Ocorrencia import Ocorrencia


class Empresa:
    def __init__(self, nome: str):
        if nome == "":
            raise ValueError()
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionar_funcionario(self, funcionário: Funcionario):
        for funcionario_lista in self.funcionarios:
            if funcionario_lista.cpf == funcionário.cpf:
                raise ValueError()
        self.funcionarios.append(funcionário)

    def adicionar_projeto(self, projeto: Projeto):
        for projeto_lista in self.projetos:
            if projeto_lista.nome == projeto.nome:
                raise ValueError()
        for colaborador in projeto.colaboradores:
            encontrou = False
            for funcionario_lista in self.funcionarios:
                if funcionario_lista.cpf == colaborador.cpf:
                    encontrou = True
            if not encontrou:
                raise ValueError()
        self.projetos.append(projeto)
