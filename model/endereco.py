from helpers.database import db

class Endereco(db.Model):

    def __init__(self, id, cep, numero, complemento, endereco, referencia, logradouro):
        self.id = id
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.endereco = endereco
        self.referencia = referencia
        self.logradouro= logradouro

    def __repr__(self):
        return '<Id: {}, CEP: {} , Número: {}, Complemento: {} , Endereco: {}, Referência: {}, Logradouro: {}>'.format(self.id, self.cep, self.numero, self.complemento, self.endereco, self.endereco, self.referencia, self.logradouro)
