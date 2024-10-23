from src.Funcionario import Funcionario


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
