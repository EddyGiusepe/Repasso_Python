'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import pandas as pd
import matplotlib.pyplot as plt

"""
Lendo de um arquivo de texto
"""
with open('./annual-real-gnp-us-1909-to-1970.txt', 'r') as f:
    # Usando a expressão regular para o separador indicando que eles são os
    # espaços em braco
    df = pd.read_table(f, sep='\s+')
    print(df)

print("\033[033mSem colocar o separador:\033[m")

with open('./annual-real-gnp-us-1909-to-1970.txt', 'r') as f:
    df = pd.read_table(f)
    print(df)