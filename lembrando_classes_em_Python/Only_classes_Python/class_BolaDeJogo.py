'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
class BolaDeJogo:
    """Classe que descreve uma Bola de Jogo"""
    def __init__(self, cor, material, raio):
        self.cor = cor
        self.material = material
        self.raio = raio

    def chutar(self):
        print("A bola foi chutada")

    def correr(self):
        print("A bola está rodando")

print("Instanciamos a nossa classe: ")

bola = BolaDeJogo("Branco com preto", "couro", 5)

bola.chutar()
print('')
bola.correr()
