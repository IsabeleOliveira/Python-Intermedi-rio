from time import time


def velocidade_execucao(funcao):
    """
    Função decoradora: Verifica o tempo que uma função leva para executar
    """
    def adiciona(*args, **kwargs):
        """ Função que adiciona e executa outra função """
        # Tempo inicial
        start = time()
        # Executa a função
        resultado = funcao(*args, **kwargs)
        # Tempo final
        end = time()
        # Resultado de tempo em ms
        tempo = (end - start) * 1000
        # Mostra o tempo
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return adiciona


@velocidade_execucao
def demora(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
demora(4)