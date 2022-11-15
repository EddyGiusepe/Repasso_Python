'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
######################################
import time
import getpass
import multiprocessing
import platform
import os

print(os.name)

print(platform.system())

print(platform.release())


######################################
#from subprocess import call

#print(call(['ping', 'google.com']))


######################################

print(multiprocessing.cpu_count())


######################################

print(getpass.getuser())

######################################


def somar_range(n):
    '''função soma vários valores num range'''
    t_0 = time.time()

    soma = 0

    for i in range(1, n + 1):
        soma += i

    t_1 = time.time()

    return soma, (t_1 - t_0)


n = 100000
print(somar_range(n))

n = 1000000
print(somar_range(n))

#########################################
# Aqui vamos a obter a informação de direitos de Autor de um Módulo
import sys
import tqdm

print(sys.copyright)


#########################################
# A seguir vamos a calcular o ponto Médio de uma reta


class Ponto:
    """
    Esta classe será apenas uma instância do meus pontos.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '({}, {})'.format(self.x, self.y)


def ponto_medio(ponto1, ponto2):
    """
    Calcula o médio da reta.
    """
    x = (ponto1.x + ponto2.x) / 2
    y = (ponto1.y + ponto2.y) / 2

    return Ponto(x, y)


# Sejam os pontos:
ponto_1 = Ponto(5, 6)
ponto_2 = Ponto(2, 2)

m = ponto_medio(ponto_1, ponto_2)

print(m)
