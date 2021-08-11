descrição = 'JOKENPÔ!!!'
aula = 'DESAFIO 45 / AULA 12'
print('\033[1;34;m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m\n')

from random import choice
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
jogador = str(input('Pedra, Papel ou Tesoura???')).strip()
jogador = jogador.capitalize()
if jogador in lista:
    print('\033[1;34mJO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!\033[m')
    sleep(1)
    print('Eu escolhi \033[34m{}\033[m e você escolheu \033[34m{}\033[m'.format(pc, jogador))
    if (pc == 'Pedra' and jogador == 'Tesoura') or (pc == 'Papel' and jogador == 'Pedra') or \
            (pc == 'Tesoura' and jogador == 'Papel'):
        print('Eu venci hahaha! Tente novamente...')
    elif pc == jogador:
        print('Deu empate hahaha! Vamos novamente.')
    else:
        print('Parabéns! Você venceu!')

else:
    print('\033[31mJogada invalida! Escolha entre Pedra, Papel e Tesoura!\033[m')
