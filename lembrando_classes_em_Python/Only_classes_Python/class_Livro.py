'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def descricao(self):
        return self.titulo + " de " + self.autor + " é composto por " + str(self.num_paginas) + " páginas."

    def ler(self, paginas_lidas):
        self.num_paginas = self.num_paginas - paginas_lidas # self.páginas -= páginas_lidas
 

print("Vamos a instanciar nossa Classe: ")

livro = Livro("A menina do cabelo azul", "Karina Gonçalves", 50)
print(livro.descricao())
livro.ler(20)
print("As páginas que me faltão ler são:", livro.num_paginas)
