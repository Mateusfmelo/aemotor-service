from helpers.database import db

class Endereco(db.Model):
    
    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario', 'concrete': True}
    
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(30), nullable=False)
    referencia = db.Column(db.String(300), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)

    pessoa_parent = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    instituicaoDeEnsino_parent = db.Column(db.Integer, db.ForeignKey("tb_instituicaoDeEnsino.id"))

    def __init__(self, cep, numero, complemento, endereco, referencia, logradouro):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.endereco = endereco
        self.referencia = referencia
        self.logradouro= logradouro

    def __repr__(self):
        return '<CEP: {}, Número: {}, Complemento: {}, Endereco: {}, Referência: {}, Logradouro: {}>'.format(self.cep, self.numero, self.complemento, self.endereco, self.referencia, self.logradouro)
