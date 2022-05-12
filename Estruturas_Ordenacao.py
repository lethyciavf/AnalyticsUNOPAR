import random

lista = [10, 4, 1, 15, -3]

lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()

print('lista = ', lista, '\n')
print('lista ordenada um = ', lista_ordenada1)
print('lista ordenada dois = ', lista_ordenada2)
print('lista = ', lista)

lista2 = []
for x in range(6):
    lista2.append(random.randint(0,100))
print('segunda lista: ', lista2)

print(sorted(lista2)) #Não Modifica lista2, apenas apresenta ordenada, a menos que seja guardada na var
print('resultado após usar Sorted: ', lista2)

print(lista2.sort()) #Modifica lista2
print('resultado da lista após .sort(): ', lista2)