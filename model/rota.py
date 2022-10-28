class Rota():

    def __init__(self, nomeDestino, qtdAlunos, prefeitura, veiculo, passageiro, horaSaida, horaChegada):
        self.nomeDestino = nomeDestino
        self.qtdAlunos = qtdAlunos
        self.prefeitura = prefeitura
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada

    def __repr__(self):
        return '<Destino: {}, Quantidade de Alunos: {}, Prefeitura: {}, Veículo: {}, Passageiro: {}, Hora de Saída: {}, Hora de Chegada: {}>'.format(self.nomeDestino, self.qtdAlunos, self.prefeitura, self.veiculo, self.passageiro, self.horaSaida, self.horaChegada)