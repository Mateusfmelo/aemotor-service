from helpers.database import db

class InstituicaoDeEnsino(db.Model):

    def __init__(self, id, endereco, telefone, nome):
        self.id = id
        self.endereco = endereco
        self.telefone = telefone
        self.nome= nome

    def __repr__(self):
        return '<Id: {} , Endereço: {} , Telefone: {}, Nome: {}>'.format(self.id, self.endereco, self.telefone, self.nome)
