'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Link de estudo --> https://cadernoscicomp.com.br/tutorial/matplot-e-pandas/pandas-lendo-arquivos-texto-csv-matplot-inserindo-anotacoes-e-texto-no-grafico/
import pandas as pd
import matplotlib.pyplot as plt

"""
Lendo um arquivo .csv com pandas e criando um pandas data frame
"""
dataframe = pd.read_csv('./annual-real-gnp-us-1909-to-1970.csv')

plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year', size=22, c='r')
plt.ylabel('GNP', size=22, c='r')
plt.title('Annual Real USA GNP 1909 to 1970', size=25, c='b')
plt.grid(True)
#plt.savefig('annual-real-gnp-us-1909-to-1970.png')
plt.show()
plt.close()