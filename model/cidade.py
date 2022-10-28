from helpers.database import db

class Cidade(db.Model):

    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla

    def __repr__(self):
        return '<Id: {} , Nome: {} , Sigla: {}>'.format(self.id, self.nome, self.sigla)