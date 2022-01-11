"""
Faça uma lista de tarefas com as seguintes opções:
    - adicionar tarefa
    - listar tarefas
    - opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    - opção de refazer (a cada vez que chamarmos, refaz a última ação)
"""

OPCOES_VALIDAS = 'ALDRS'


def menu_movimentos():
    print("----------------MENU----------------")
    movimento_1 = '[A] - ADICIONAR TAREFA'
    movimento_2 = '[L] - LISTAR TAREFAS'
    movimento_3 = '[D] - DESFAZER AÇÃO'
    movimento_4 = '[R] - REFAZER AÇÃO'
    movimento_5 = '[S] - SAIR DA LISTA'

    print(movimento_1)
    print(movimento_2)
    print(movimento_3)
    print(movimento_4)
    print(movimento_5)

    Input = str(input("Digite o movimento: "))
    if Input in OPCOES_VALIDAS:
        return Input
    else:
        print("Esta operação é inválida, tente novamente: ")
        return menu_movimentos()


list_tarefas = []
lixo = []


def adicionar_tarefa():
    print("----------------ADICIONAR TAREFAS----------------")
    tarefas = str(input("Digite a tarefa que quer adicionar: "))
    if tarefas in list_tarefas:
        print("Essa tarefa já existe")
    else:
        list_tarefas.append(tarefas)
        print("Tarefa cadastrada com sucesso!!!")


def listar_tarefas():
    print('--------------Listar Tarefas-------------')
    print('Tarefas: ')
    print(list_tarefas)
    print()


def desfazer():
    print("---------Desfazer ação-------------")
    if not list_tarefas:
        print('Nada a desfazer')
        return

    list_new = list_tarefas.pop()
    lixo.append(list_new)


def refazer():
    print( "---------Refazer ação-------------" )
    if not lixo:
        print('Nada a refazer')
        return

    list_new = lixo.pop()
    list_tarefas.append(list_new)


if __name__ == '__main__':
    movimento = menu_movimentos()
    while movimento in OPCOES_VALIDAS:
        if movimento == 'A':
            adicionar_tarefa()
            movimento = menu_movimentos()
        elif movimento == 'L':
            listar_tarefas()
            movimento = menu_movimentos()
        elif movimento == 'D':
            desfazer()
            movimento = menu_movimentos()
        elif movimento == 'R':
            refazer()
            movimento = menu_movimentos()
        elif movimento == 'S':
            print("A lista de tarefas irá ser fechada!!!")
            break
        else:
            print("Esta operação não existe, tente novamente: ")
            movimento = menu_movimentos()



