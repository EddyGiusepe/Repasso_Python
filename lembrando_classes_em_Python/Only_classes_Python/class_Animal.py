'''
Dr.Eddy Giusepe Chirinos Isidro 
'''
class Animal:
    def __init__(self, nome, especie, som):
        self.nome = nome
        self.especie = especie
        self.som = som

    def fazer_som(self): # Este é um método
        return self.som


cachorro = Animal("Black", "Biralata", "Uau Uau")

gato = Animal("Gatuno", "Angora", "Miau Miau")



print("Agora chamamos a nossa Classe: ")

print(cachorro.nome + " é um " + cachorro.especie + " que faz " + cachorro.fazer_som())
print('')
print(gato.nome + " é um " + gato.especie + " que faz " + gato.fazer_som())
