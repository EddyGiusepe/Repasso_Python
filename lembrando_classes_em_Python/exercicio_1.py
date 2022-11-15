'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''


class Persona:
    '''Classe que tem Dados de uma pessoa'''

    def __init__(self, nome, idade, e_mail):
        self.nome = nome
        self.idade = idade
        self.e_mail = e_mail

    def __str__(self) -> str:
        '''Método que printa esses Dados'''
        return "Nome: {}\nIdade: {}\ne-mail: {}".format(self.nome, self.idade, self.e_mail)


eddy = Persona('Eddy', 41, 'eddy_chirinos@outlook.com')
print(eddy)
