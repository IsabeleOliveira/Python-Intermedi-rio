import re
import random

REGRESSIVO = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = remove_caracteres(cnpj)

    try:
        if sequencia(cnpj):
            return False
    except:
        return False

    try:
        new_cnpj = calcular_digitos(cnpj=cnpj, digito=1)
        new_cnpj = calcular_digitos(cnpj=new_cnpj, digito=2)
    except Exception as e:
        return False

    if new_cnpj == cnpj:
        return True
    else:
        return False


def calcular_digitos(cnpj, digito):
    if digito == 1:
        i = REGRESSIVO[1:]
        new_cnpj = cnpj[:-2]
    elif digito == 2:
        i = REGRESSIVO
        new_cnpj = cnpj
    else:
        return None


    total = 0
    for indice, i in enumerate(i):
        total += int(cnpj[indice]) * i

    digito = 11 - (total % 11)# verificar os dígitos
    digito = digito if digito <= 9 else 0

    return f'{new_cnpj}{digito}'


def sequencia(cnpj):
    seq = cnpj[0] * len(cnpj)

    if seq == cnpj:
        return True
    else:
        return False


def remove_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def gerar_cnpj():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'

    new_cnpj = calcular_digitos(cnpj=inicio_cnpj, digito=1)
    new_cnpj = calcular_digitos(cnpj=new_cnpj, digito=2)

    return new_cnpj


def formatar_cnpj(cnpj):
    cnpj = remove_caracteres(cnpj)
    formatar = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatar

