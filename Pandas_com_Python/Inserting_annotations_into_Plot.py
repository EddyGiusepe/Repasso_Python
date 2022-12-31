'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import pandas as pd
import matplotlib.pyplot as plt

"""
Incluindo annotates
"""
dataframe = pd.read_csv('annual-real-gnp-us-1909-to-1970.csv')

plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year', size=22, c='r')
plt.ylabel('GNP', size=22, c='r')
plt.title('Annual Real USA GNP 1909 to 1970', size=25, c='b')
plt.grid(True, c='pink')
# matplotlib.pyplot.annotate(*args, **kwargs)
# s:str - The text of the annotation
# xy:iterable - Length 2 sequence specifying the (x,y) point to annotate
# xytext : iterable, optional - Length 2 sequence specifying the (x,y)
#          to place the text at. If None, defaults to xy.
# arrowprops: dict, optional
plt.annotate('Fim da Segunda Gerra Mundial', xy=(1945, 355.2),
             arrowprops=dict(arrowstyle='->'), xytext=(1915, 300))
plt.annotate('Crash da Bolsa', xy=(1929, 203.6),
             arrowprops=dict(arrowstyle='->'), xytext=(1909, 200))

#plt.savefig('gnp-us-1909-to-1970-annotate.png')
plt.show()
plt.close()