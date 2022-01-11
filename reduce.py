from map import lista, produtos, pessoas
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_produtos = reduce(lambda ac, i: i['preço'] + ac, produtos, 0)
print(soma_produtos)

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade)
