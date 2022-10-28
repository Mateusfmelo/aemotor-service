class Endereco():

    def __init__(self, cep, numero, complemento, endereco, referencia, logradouro):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.endereco = endereco
        self.referencia = referencia
        self.logradouro= logradouro

    def __repr__(self):
        return '<CEP: {}, Número: {}, Complemento: {}, Endereco: {}, Referência: {}, Logradouro: {}>'.format(self.cep, self.numero, self.complemento, self.endereco, self.referencia, self.logradouro)
