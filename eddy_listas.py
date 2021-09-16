# Data Scientist Jr. Eddy Giusepe Chirinos Isidro
# Link: https://www.youtube.com/watch?v=N1hTsbW50eM&t=2s
from typing import List


print("###################################################################")
print("## A seguir mostramos alguns exemplos do uso de Listas em PYthon ##")
print("###################################################################")


print("###############")
print("## Exemplo_1 ##")
print("###############")

print("Criamos a nossa lista, assim: ")
lista = [2.6, 5, 9, 1.9, -3, 8, 0]
# Pode, também, ser criada assim:
#lista1 = list(range(4, 11))
print(lista)
print("")
print("Ordenamos a nossa lista:")
lista.sort()
print("Agora imprimimos a nossa lista ordenada: ")
print(lista)
print("Podemos ordenar de forma decrescente, assim: ")
lista.sort(reverse=True)
print(lista)
print("Vejamos o tamnaho da nossa lista: ")
print(len(lista))


print("###############")
print("## Exemplo_2 ##")
print("###############")

print("Suponhamos que temos a seguinte lista")
lista1 = [2, 5, 9, 1]
print(lista1)
print("Trocamos o número '9' da lista assim: ")
lista1[2]=3
print(lista1)
print("Adicionamos algúm elemento a nossa lista, assim: ")
lista1.append(7)
print("A  nossa lista1 com o novo valor é: ")
print(lista1)
print("Agora, em nossa lista1 vamos a insertar um novo valor em qualquer posição: ")
lista1.insert(2, 50) # posição-->2  ; valor novo --> 50
print(lista1)
print("Da nossa atual lista, vou eliminar o número '1' da posição '4', assim:")
lista1.pop(4)
print(lista1)





