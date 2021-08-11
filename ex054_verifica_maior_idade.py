aula = 'DESAFIO 54 / AULA 13'
descrição = 'Verifica quem é maoir de idade. Considerando 21 anos.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')
from datetime import date

atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo {} são maiores de idade e {} são menores'.format(maior, menor))
