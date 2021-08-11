descrição = 'Contagem Regressiva para Fogos de Artifício.'
aula = 'DESAFIO 46 / AULA 13'
print('\033[1;34;m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m\n')
from time import sleep

play = int(input('Digite 1 para iniciar a contagem: '))
if play > 0:
    for c in range(11, -1, -1):
        print(c)
        sleep(1)
        if c == 1:
            print('\033[31mBUUUOOM!!!\033[m')
