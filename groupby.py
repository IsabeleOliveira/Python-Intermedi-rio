from itertools import groupby

lista1 = [
    {'nome': 'Isabele', 'nota': '2'},
    {'nome': 'Rose', 'nota': '5'},
    {'nome': 'Mariana', 'nota': '3'},
    {'nome': 'Lucas', 'nota': '7'},
    {'nome': 'Davi', 'nota': '5'},
    {'nome': 'Marina', 'nota': '8'},
]


lista1_ordem = lambda item2: item2['nota']
lista1.sort(key=lista1_ordem)
lista1_agrupados = groupby(lista1, lista1_ordem)


for i, j in lista1_agrupados:
    print(f'Agrumamento {i}')
    quantidade = (len(list(j)))
    print(f'{quantidade} alunos tiraram a nota {i}')



