'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Vamos a calcular a distância entre dois pontos cartesianos.
# P1(x1, y1) e P2(x2, y2)

from math import sqrt


class Ponto:
    '''Elementos de um par ordenado'''

    def __init__(self, x, y):
        self.x = x
        self.y = y


def calcula_distancia(p1, p2):
    '''Esta função recebe os pontos cartesianos'''
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


# Nossos pontos:
ponto1 = Ponto(5, 6)
ponto2 = Ponto(2, 2)

print(calcula_distancia(ponto1, ponto2))
