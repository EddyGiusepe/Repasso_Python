'''
Dr.Eddy Giusepe Chirinos Isidro 
'''
import pandas as pd
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, path_arquivo):
        self.dados = pd.read_csv(path_arquivo)

    def plotar(self, coluna_x, coluna_y):
        fig = plt.figure(figsize=(8, 12))
        plt.title("Estoque numa loja de varejo")
        plt.scatter(self.dados[coluna_x], self.dados[coluna_y], label=coluna_y, c='r', alpha=0.3)
        plt.xlabel(coluna_x)
        plt.ylabel(coluna_y)
        plt.legend()
        plt.show()


plotter = Plotter("/home/eddygiusepe/1_Eddy_Giusepe/Repasso_Python/lembrando_classes_em_Python/Only_classes_Python/estoque.csv")

plotter.plotar("Quantidade", "Valor")

