from helpers.database import db

class Pessoa(db.Model):

    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Nome: {}, Nascimento: {}, Email: {}, Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
