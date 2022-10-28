from helpers.database import db

class Prefeitura(db.Model):

    def __init__(self, id, secretarios, email, telefone, nomePrefeito):
        self.id = id
        self.secretarios = secretarios
        self.email = email
        self.telefone = telefone
        self.nomePrefeito= nomePrefeito

    def __repr__(self):
        return '<Id: {}, Secretários: {}, Email: {}, Telefone: {}, Nome do Prefeito: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.nomePrefeito)
