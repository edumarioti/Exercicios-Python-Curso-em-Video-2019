print('============ DESAFIO 17 / AULA 08 ============')
print('Calculando a Hipotenusa.\n')

import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hi = math.hypot(co, ca)

print('\nO valor da hipotenusa é: {:.2f}'.format(hi))
