'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
class SistemaSolar:
    def __init__(self, nome):
        self.nome = nome
        self.planetas = []

    def adicionar_planeta(self, planeta):
        self.planetas.append(planeta) 

    def listar_planetas(self):
        for i, planeta in enumerate(self.planetas):
            print(f"{i + 1}: {planeta.nome}") 

class Planeta:
    def __init__(self, nome, dist_sol, diametro):
        self.nome = nome
        self.dist_sol = dist_sol
        self.diametro = diametro



print("Vamos a instanciar nossa classe e ver os métodos que ela têm: ")

sistema_solar = SistemaSolar("Nosso Sistema Solar")
planeta_terra = Planeta("Terra", 149.6, 12_742)
planeta_marte = Planeta("Marte", 227.9, 6_794)
sistema_solar.adicionar_planeta(planeta_terra)
sistema_solar.adicionar_planeta(planeta_marte)
sistema_solar.listar_planetas()
