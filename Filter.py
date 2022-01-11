from map import lista, produtos



nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))


def filtra(produto):
    if produto['preço'] > 30:
        produto['é caro'] = True
    return True


print(" ")
novalista = filter(filtra, produtos)

for i in novalista:
    print(i)
