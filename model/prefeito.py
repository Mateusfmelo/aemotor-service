from helpers.database import db
from model.pessoa import Pessoa

class Prefeito(Pessoa):

    def __init__(self, nome, nascimento, email, telefone):
        super.__init__(nome, nascimento, email, telefone)


    def __repr__(self):
        return '<Nome: {}, Nascimento: {}, Email: {}, Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)