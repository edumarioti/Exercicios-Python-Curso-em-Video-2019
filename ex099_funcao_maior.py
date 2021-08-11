from time import sleep
from aux_exercicios import *


def maior(*num):
    print('Analizando os valores passados...')
    sleep(1)
    nummaior = num[0]
    for c in num:
        print(f'{c} ', end='')
        sleep(0.25)
        if nummaior < c:
            nummaior = c
    print()
    sleep(0.25)
    print(f'Foram informados \033[1;34;m{len(num)}\033[m números')
    sleep(0.25)
    print(f'O maior número é: \033[1;34;m{nummaior}\033[m')
    sleep(0.25)
    linha()


titulo(' DESAFIO 99 / AULA 20 ', 'Função verifica número maior.')

# Programa principal:
maior(1, 2, 0, 5, 4, 6)
maior(2, 5, 3, 5, 5, 9)
