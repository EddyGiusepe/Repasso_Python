'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Aqui vamos a criar uma Hierarquia (ou jerarquia) de Herença básica


class Pessoa:
    '''Classe que contém os Dados de uma pessoa'''

    def __init__(self, carteira_id, nome, e_mail):
        self.carteira_id = carteira_id
        self.nome = nome
        self.e_mail = e_mail


class Estudante(Pessoa):
    '''Classe Hereda a classe Pessoa'''

    def __init__(self, carteira_id, nome, e_mail, carnet, profissao):
        super().__init__(carteira_id, nome, e_mail)
        self.carnet = carnet
        self.profissao = profissao


eddy = Estudante("RG-123456", "Eddy Giusepe", "eddy_chirinos@outlook.com",
                 "UFES-123", "PhD.:Físico-Data Scientist")

print(isinstance(eddy, Estudante))

print(isinstance(eddy, Pessoa))

print(eddy.nome)
print(eddy.carteira_id)
print(eddy.profissao)
