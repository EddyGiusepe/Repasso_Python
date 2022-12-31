'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Link de estudo: https://cadernoscicomp.com.br/tutorial/matplot-e-pandas/pandas-lendo-arquivos-texto-csv-matplot-inserindo-anotacoes-e-texto-no-grafico/
import pandas as pd
import matplotlib.pyplot as plt

"""
Annotates dentro de um box
"""
dataframe = pd.read_csv('annual-real-gnp-us-1909-to-1970.csv')

plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year', size=20, c='r')
plt.ylabel('GNP', size=20, c='r')
plt.title('PIB EUA Real Anual de 1909 a 1970', size=25, c='b')
plt.grid(True)


# atributos para fonte:
# color - cor da fonte
# size - size in points or ['xx-small', 'x-small', 'small', 'medium', 'large',
#          'x-large', 'xx-large']
# weight - ['light' | 'ultralight' | 'normal' | 'bold' | 'heavy' | 'ultrabold'
# style - ['normal' | 'italic' | 'oblique']
# family - ['serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace']
plt.annotate(
    'Fim da Segunda Gerra Mundial',
    xy=(1945, 355.2),
    color='red',
    size='14',
    arrowprops=dict(arrowstyle='->'), xytext=(1920, 500),
    bbox = dict(boxstyle='round,pad=0.2', fc='yellow',
                alpha=0.3),
)
plt.annotate(
    'Crash da Bolsa', xy=(1929, 203.6),
    arrowprops=dict(arrowstyle='->'),
    xytext=(1909, 200),
    color='yellow',
    weight='heavy',
    style='italic',
    bbox = dict(boxstyle='round,pad=0.2', fc='red',
                alpha=1),
)
plt.savefig("gráfico_box")
plt.show()
