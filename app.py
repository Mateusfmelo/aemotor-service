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

cidade = Cidade ("01", "Guarabira", "GBA")

endereco = Endereco ("01", "58200-000", "69", "Próximo a Guaraves", "Rua Antonio Galdino Guedes", "Lanchonete Mundial", "Rua Antonio Galdino Guedes")

funcionario = Funcionario ("Marcos", "11/09/2001", "marcoscontato@gmail.com", "98785-8979", "Prefeitura Municipal de Guarabira", "Motorista")

gestorAPP = GestorAPP ("Gleidson", "01/01/2001", "gleidsontubarao@gmail.com", "98785-1423")

instituicaoDeEnsino = InstituicaoDeEnsino ("01", "Rua Professor Carlos Leonardo Arcoverde", "98195-6465", "IFPB")

motorista = Motorista ("Erick", "24/05/1992", "erickmotorista@gmail.com", "98745-6214", "Prefeitura Municipal de Solânea", "Motorista", "Solânea, Bananeiras, Belém, Pirpirituba e Guarabira")

passageiro = Passageiro ("Mateus", "06/05/2001", "mateusmelo51@gmail.com", "4002-8922", "IFPB", "TSI", "67", "João Pessoa", "Guarabira")

pessoa = Pessoa ("Mateus", "06/05/2001", "mateusmelo51@gmail.com", "4002-8922")

prefeito = Prefeito ("Marcus Diogo de Lima", "18/11/1964")

prefeitura = Prefeitura ("01", "Félix", "felix@gmail.com", "99845-7896", "Marcus Diogo de Lima")

rota = Rota ("Guarabira", "29", "Prefeitura Municipal de Solânea", "Ônibus", "Mateus", "12:40", "13:30")

uf = UF ("01", "Ônibus", "PB")

veiculo = Veiculo ("01", "Solânea", "29", "Ônibus", "XRE-300")
