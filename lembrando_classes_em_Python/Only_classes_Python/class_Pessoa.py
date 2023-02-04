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
