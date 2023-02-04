'''
Dr.Eddy Giusepe Chirinos Isidro 
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def saudacao(self):
        return "Olá, meu nome é " + self.nome + "!"


print("Vejamos o uso de nossa class simples: ")

pessoa = Pessoa("Eddy Giusepe", 41)

print(pessoa.nome)
print('')
print(pessoa.idade)
print('')
print(pessoa.saudacao())


print("######################################################")

class Pessoa:
    '''Classe para dar informações de uma pessoa'''
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def cumprimentar(self):
        return "Olá, meu nome é " + self.nome

    def informacoes(self):
        return "Nome: " + self.nome + ", Idade: " + str(self.idade) + ", Endereço: " + self.endereco

pessoa1 = Pessoa("João", 30, "Rua das Flores, 123")
pessoa2 = Pessoa("Maria", 25, "Rua dos Jardins, 456")

print(pessoa1.cumprimentar())
print(pessoa1.informacoes())

print(pessoa2.cumprimentar())
print(pessoa2.informacoes())