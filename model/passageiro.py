from helpers.database import db

from model.pessoa import Aluno

class Passageiro(Aluno):

    def __init__(self, nome, nascimento, email, telefone, InstituicaoDeEnsino, curso, matricula, cidadeOrigem, cidadeDestino):
        super.__init__(nome, nascimento, email, telefone, InstituicaoDeEnsino, curso, matricula)
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return '<Nome: {}, Nascimento: {} , Email:{}, Telefone:{} , Instituição de Ensino: {}, Curso: {}, Matricula: {}, Cidade de Origem: {}, Cidade de Destino: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula, self.cidadeOrigem, self.cidadeDestino)