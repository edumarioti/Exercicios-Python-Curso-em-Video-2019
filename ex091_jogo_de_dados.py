aula = ' DESAFIO 91 / AULA 19 '
descrição = 'Jogo de dados (Ordenando dicionario).'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')

from random import randint
from time import sleep
from operator import itemgetter
ranking = dict()
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('\033[34m- - - VALORES SORTEADOS - - -\033[m')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou \033[1;34;m{v}\033[m no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\033[34m=' * tamanho + '\033[m')
print('\033[34m- - - RANKING DOS JOGADORES - - -\033[m')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'\033[34m{i+1}º\033[m lugar: {v[0]} com \033[34m{v[1]}\033[m')