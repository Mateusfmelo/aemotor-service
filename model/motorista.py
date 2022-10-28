from model.funcionario import Funcionario

class Motorista(Funcionario):

    def __init__(self, rotas):
        self.rotas = rotas

    def __repr__(self):
        return 'Rotas: {}'.format(self.rotas)