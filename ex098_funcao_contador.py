from aux_exercicios import *

titulo(' DESAFIO 98 / AULA 20 ', ' Função para contagem. ')

from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        print('Passo no valor Zero não é permitido!')
        print('Utilizando valor 1 no passo.')
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} á {fim} de {passo} em {passo}:')
    sleep(1)
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.25)
        print('Fim.')
        linha()
        sleep(0.25)
    else:
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.25)
        print('Fim.')
        linha()
        sleep(0.25)


# Pragrama Principal
contador(1, 10, 1)
contador(10, 1, 2)
print('Agora é sua vez personalizar a contagem:')
i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
linha()
contador(i, f, p)
