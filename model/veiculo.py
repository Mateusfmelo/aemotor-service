from helpers.database import db

class Veiculo(db.Model):

    def __init__(self, id, cidade, qtdPassageiros, tipoVeiculo, placa):
        self.id = id
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa

    def __repr__(self):
        return '<Id: {}, Cidade: {}, Quantidade de Passageiros: {}, Veículo: {}, Placa: {}>'.format(self.id, self.cidade, self.qtdPassageiros, self.tipoVeiculo, self.placa)