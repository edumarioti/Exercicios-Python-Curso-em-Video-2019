print('============ DESAFIO 18 / AULA 08 ============')
print('Calculo de SENO, COSSENO e TANGENTE\n')

import math

a = float(input('Digite o angulo desejado: '))

x = math.radians(a)
print('\nO seu SENO é de: {:.2f}'.format(math.sin(x)))
print('O seu COSSENO é de: {:.2f}'.format(math.cos(x)))
print('A sua TANGENTE é de: {:.2f}'.format(math.tan(x)))
