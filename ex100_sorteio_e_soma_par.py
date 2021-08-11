from random import randint
from aux_exercicios import *

def sorteio(lista):
    print('Os valores sorteados são: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[c]} ', end='')
    print()


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Soma dos valores pares de {lista}, é: {soma}')


# Cabeçalho:
titulo(' DESAFIO 100 / AULA 20 ',
       'Função Sorteia números e soma os pares.')

numeros = list()
sorteio(numeros)
somapar(numeros)
linha()