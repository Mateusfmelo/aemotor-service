from model.aluno import Aluno
from model.cidade import Cidade
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.gestorAPP import GestorAPP
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import UF
from model.veiculo import Veiculo

aluno = Aluno ("Mateus", "06/05/2001", "mateusmelo51@gmail.com", "4002-8922", "IFPB", "TSI", "67")
print(aluno)

cidade = Cidade ("Guarabira", "GBA")
print(cidade)

endereco = Endereco ("58200-000", "69", "Próximo a Guaraves", "Rua Antonio Galdino Guedes", "Lanchonete Mundial", "Rua Antonio Galdino Guedes")
print(endereco)

funcionario = Funcionario ("Déris", "15/07/1980", "deris@gmail.com", "98745-9831","Prefeitura Municipal de Guarabira", "Segurança")
print(funcionario)

gestorAPP = GestorAPP ("Gleidson")
print(gestorAPP)

instituicaoDeEnsino = InstituicaoDeEnsino ("IFPB", "Rua Professor Carlos Leonardo Arcoverde", "98195-6465")
print(instituicaoDeEnsino)

motorista = Motorista ("Erick", "15/07/1980", "erick@gmail.com", "98745-9831","Prefeitura Municipal de Solânea", "Motorista","Solânea, Bananeiras, Belém, Pirpirituba e Guarabira")
print(motorista)

passageiro = Passageiro ("Mateus", "06/05/2001", "mateusmelo51@gmail.com", "4002-8922", "IFPB", "67", "TSI", "João Pessoa", "Guarabira")
print(passageiro)

pessoa = Pessoa ("Mateus", "06/05/2001", "mateusmelo51@gmail.com", "4002-8922")
print(pessoa)

prefeito = Prefeito ("Marcus Diogo de Lima", "18/11/1964", "marcus@gmail.com", "3271-1946")
print(prefeito)

prefeitura = Prefeitura ("Félix", "felix@gmail.com", "99845-7896", "Marcus Diogo de Lima")
print(prefeitura)

rota = Rota ("Guarabira", "29", "Prefeitura Municipal de Solânea", "Ônibus", "Mateus", "12:40", "13:30")
print(rota)

uf = UF ("Paraíba", "PB")
print(uf)

veiculo = Veiculo ("Solânea", "29", "Ônibus", "XRE-300")
print(veiculo)
