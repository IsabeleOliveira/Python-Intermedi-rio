import time


def gerador():
    r = []
    for j in range(100):
        yield j
        time.sleep(0.1)
    return r


g = gerador()


for i in g:
    print(i)

