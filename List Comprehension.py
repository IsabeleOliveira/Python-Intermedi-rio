"""
string = '0123456789012345678901234567890123456789'
lista = ['0123456789','0123456789','0123456789', '0123456789']
retorno = '0123456789.0123456789.0123456789.0123456789'
"""
string = '0123456789012345678901234567890123456789'
numero = 10
count = [i for i in range(0, len(string), numero)]  # uma lista comprehension
lista = [string[i: i + numero] for i in range(0, len(string), numero)]
retorno = '.'.join(lista)  # vai ficar no formato pedido pela questão, já q a função join ela separa (".")
print(lista)
print(retorno)




