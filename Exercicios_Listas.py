"""
1 - Crie uma função que encontra o primeiro duplicado, considerando o segundo número
como duplicação. Retorne a duplicação considerada

"""
lista_numeros_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]



def num_duplicado(param_lista_numeros_inteiros):
    numeros_check = set()
    primeiro_duplicado = -1

    for i in param_lista_numeros_inteiros:
        if i in numeros_check:
            primeiro_duplicado = i
            break

        numeros_check.add(i)



    return primeiro_duplicado


for lista in lista_numeros_inteiros:
    print(lista, num_duplicado(lista))

"""

2 - Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

----resultado----
lista_soma  = [2, 4, 6, 8]

"""


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_final = sum([v1 + v2 for v1, v2 in zip(lista_a, lista_b)])
print(lista_final)

lista_final = []
for i in range(len(lista_b)):
     lista_final.append(lista_a[i] + lista_b[i])
print(lista_final)
