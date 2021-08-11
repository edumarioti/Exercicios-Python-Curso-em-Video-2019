aula = 'DESAFIO 68 / AULA 15'
descrição = 'Jogo impar ou par (Breack)'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')


from random import randint
c = 0
print('Sou o Computador e quero jogar com você!')
while True:
    pc = randint(0, 10)
    jogador = int(input('Escolha um numero:'))
    total = jogador + pc
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Escolha Par ou Impar [P/I]:').upper().strip()[0])
    print(f'Você jogou \033[34m{jogador}\033[m e eu \033[34m{pc}\033[m. Total de \033[34m{(total)}\033[m')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if parouimpar == 'P' :
        if total % 2 == 0:
            print('Você ganhou!!!')
            c += 1
        else:
            print('Você perdeu.')
            break
    if parouimpar == 'I':
        if total % 2 == 1:
            print('Você ganhou!!!')
            c += 1
        else:
            print('Você perdeu.')
            break
    print('Vamos jogar de novo!\n')
    print('\033[34m=\033[m'*50)
print(f'Você ganhou um total de \033[34m{c}\033[m vezes!')
