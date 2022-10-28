from model.pessoa import Pessoa

class GestorAPP(Pessoa):

    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return '<Gestor do Aplicativo: {}>'.format(self.pessoa)