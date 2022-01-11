perguntas = {
    'Perguntas 1': {
        'pergunta': 'Quanto é 2+2',
        'respostas': {'a': '1', 'b': '2', 'c': '4'},
        'resposta certa': 'c',
    },
    'Perguntas 2': {
        'pergunta': 'Quanto é 5+2',
        'respostas': {'a': '7', 'b': '2', 'c': '4'},
        'resposta certa': 'a',
    },
    'Perguntas 3': {
        'pergunta': 'Quanto é 7*7',
        'respostas': {'a': '7', 'b': '49', 'c': '40'},
        'resposta certa': 'b',
    },

}
print()


resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas')
    for rk, rv in pv['respostas'].items():
        print(f'{rk}: {rv}')

    resposta_usuario = input("Digite sua resposta: ")

    if resposta_usuario == pv['resposta certa']:
        print('UHUUUL, SUA RESPOSTA ESTÁ CERTA')
        resposta_certa += 1
    else:
        print('TURURUU, SUA RESPOSTA ESTÁ ERRADA')

    print()


qtd_perguntas = len(perguntas)
porcetagem_acertos = resposta_certa / qtd_perguntas * 100.0

print(f'Voce acertou {resposta_certa} respostas')
print(f'Sua porcentagem de acertos foi de {porcetagem_acertos}%')

