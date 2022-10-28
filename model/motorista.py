from helpers.database import db
from model.funcionario import Funcionario
from model.pessoa import Funcionario

class Motorista(Funcionario):

    def __init__(self, nome, nascimento, email, telefone, prefeitura, cargo, rotas):
        super.__init__(nome, nascimento, email, telefone, prefeitura, cargo)
        self.rotas = rotas

    def __repr__(self):
        return '<Nome: {}, Nascimento: {}, Email: {}, Telefone: {}, Prefeitura: {}, Cargo: {}>, Rotas: {}'.format(self.nome, self.nascimento, self.email, self.telefone, self.prefeitura, self.cargo, self.rotas)