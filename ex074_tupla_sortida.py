aula = 'DESAFIO 74 / AULA 16'
descrição = 'Tupla Sortida.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
print('Os números sorteados são: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO número maior é o {max(tupla)} e o menor é o {min(tupla)}')
