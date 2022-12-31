'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import pandas as pd
import matplotlib.pyplot as plt

"""
Incluindo texto no gráfico
"""
dataframe = pd.read_csv('annual-real-gnp-us-1909-to-1970.csv')

font_1 = {'family':'serif', 'color':'#FFFC19', 'fontsize':'large' }
font_2 = {'family':'fantasy', 'color':'yellow', 'size':'16'}
font_3 = {'family':'serif', 'color':'yellow', 'size':'18', 'weight':'bold'}

plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year', size=22, c='r')
plt.ylabel('GNP', size=22, c='r')
plt.title('Annual Real USA GNP 1909 to 1970', size=22, c='b')
plt.grid(True)

plt.annotate('Fim da Segunda Gerra Mundial', xy=(1945, 355.2),
             arrowprops=dict(arrowstyle='->'), xytext=(1920, 300))
plt.annotate('Crash da Bolsa', xy=(1929, 203.6),
             arrowprops=dict(arrowstyle='->'), xytext=(1909, 200))

# class matplotlib.text.Annotation(s, xy, xytext=None, xycoords='data',
#   textcoords=None, arrowprops=None, annotation_clip=None, **kwargs)
plt.text(1909, 500, 'Pequeno texto de exemplo 1', fontdict=font_1,
         backgroundcolor='#0971B2')

plt.text(1909, 600, 'Pequeno texto de exemplo 2', fontdict=font_2,
         backgroundcolor='#000000')

# horizontalalignment or ha ['center' | 'right' | 'left']
# verticalalignment or va ['center' | 'top' | 'bottom' | 'baseline']
plt.text(1940, 700, 'Pequeno texto de exemplo 3', fontdict=font_3,
         backgroundcolor='#000000', horizontalalignment='center',
         verticalalignment='top')

plt.savefig('gnp-us-1909-to-1970-text.png')
plt.show()
plt.close()