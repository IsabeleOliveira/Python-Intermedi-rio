from map import pessoas, produtos


pessoa = map(lambda item: item['nome'], pessoas)
for i in pessoa:
    print(i)

print("")

produto = map(lambda item: item['preço'], produtos)
for j in produto:
    print(j)
