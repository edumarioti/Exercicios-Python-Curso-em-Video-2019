aula = 'DESAFIO 58 / AULA 14'
descrição = 'Jogo da adivinhação, entre 0 e 10.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

from random import randint
print('Escolhi um numero de 0 a 10.\nVocê consegue adivinhar qual é?\n')
pc = randint(0, 10)
t = 0
correto = False
while not correto:
    jogador = int(input('Qual seu palpite??\n'))
    t += 1
    if jogador <= 10:
        if jogador == pc:
            correto = True
        elif pc > jogador:
            print('É um numero \033[34mMAIOR...\033[m Tente mais uma vez! ')
        else:
            print('É um numero \033[34mMENOR...\033[m Tente mais uma vez! ')
    else:
        print('O numero \033[34m{}\033[m não esté entre 0 e 10, Tente novamente:')

print('Você acertou com {} tentativas, Parabéns!'.format(t))


