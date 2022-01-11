"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome:
"""

print("------Questão 1---------")


def saudacao(msg, nome):
    print(msg, nome)


msg = "Olá"
nome1 = str(input("Digite seu nome: "))

saudacao(msg, nome=nome1)

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""

print("------Questão 2---------")


def soma_numeros(num1, num2, num3):
    print(num1 + num2 + num3)


val1 = int(input("Digite um número: "))
val2 = int(input("Digite outro número: "))
val3 = int(input("Digite outro número: "))

soma_numeros(num1=val1, num2=val2, num3=val3)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual
(ex: 10%). Retorne (return) o valor do primeiro número somado do aumento do percentual
do mesmo.
"""

print("------Questão 3---------")


def soma_percentual(num1, num2):
    val_final = num1 + (num1 * num2/100)
    return val_final


val = int(input("Digite um valor: "))
porcentagem = int(input("Digite uma porcentagem: "))


sp = soma_percentual(num1=val, num2=porcentagem)
print(sp)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for
divisível por 5 e 3, retorne FizzBuzz, caso contrário, retorne o número enviado. 
"""

print("------Questão 4---------")


def fizzbuzz(num):
    if (num % 5 == 0) and (num % 3 == 0):
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 2 == 0:
        return "Fizz"
    else:
        return num


numero = int(input("Digite um valor: "))


fb = fizzbuzz(num=numero)
print(fb)

"""
5 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor 
da função2 executada
"""
print("------Questão 5---------")


def func1():
    return 'Olá usuário!'


def func2(func1):
    return func1()


print('Olá usuário()')


"""
6 - Crie uma função1 que receba uma função2 como parâmetro e retorne o valor
da função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumento.

"""

print("------Questão 6---------")

def funcao1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def ola_usuario(nome):
    return f'Oi {nome}'


def saudacoes(nome, msg):
    return f'{msg} {nome}'


funfando = funcao1(ola_usuario, 'Isabele')
funfando2 = funcao1(saudacoes, 'Isabele', msg='Boa tarde,')
print(funfando)
print(funfando2)
