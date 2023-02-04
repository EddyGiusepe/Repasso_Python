'''
Dr.Eddy Giusepe Chirinos Isidro 
'''

class Carro:
    '''Características de um Carro'''
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
        
        self.velocidade = 0

    def acelerar(self, kmh):
        self.velocidade += kmh

    def frear(self, kmh):
        self.velocidade -= kmh

    def velocidade_atual(self):
        return self.velocidade


print("Vamos ver agora o funcionamento da minha Classe: ")                    
print('')
carro = Carro("Toyota", "Camry", 2022)

print(carro.marca)
print(carro.modelo)
print(carro.ano)

print(carro.velocidade_atual())

carro.acelerar(50)
print(carro.velocidade_atual())

carro.frear(30)
print(carro.velocidade_atual())
