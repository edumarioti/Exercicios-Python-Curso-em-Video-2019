from random import randint
from time import sleep
print('============ DESAFIO 28 / AULA 10 ============')
print('Adivinhe o numero escolhido de 0 à 5\n')
computador = randint(0, 5)
jogador = int(input('Já pensou qual o numero? Diz aí: '))
print('PROCESSANDO...')
sleep(1)

if computador == jogador:
    print('Parabéns! Você acertou!!!')
else:
    print('A que pena, você errou')
    print('O numero correto é: {}'.format(computador))


