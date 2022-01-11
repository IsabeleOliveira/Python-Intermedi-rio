carrinho = []


carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))


soma = sum([int(i2) for i1, i2 in carrinho])
print(soma)