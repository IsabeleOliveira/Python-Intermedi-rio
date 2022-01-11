from itertools import count

contador = count()
lista = ['Isabele', 'Davi', 'Lucas']

lista = zip(contador, lista)
print(list(lista))

