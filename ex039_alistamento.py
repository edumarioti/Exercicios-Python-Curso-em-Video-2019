descrição = 'Sistema de Alistamento'
aula = 'DESAFIO 39 / AULA 12'
print('\033[34m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m')

import datetime

atual = datetime.date.today().year
nascimento = int(input('Qual o ano do seu nascimento? '))
idade = atual - nascimento
if idade < 18:
    print('Seu alistamento deve acontecer em {} ano(s).'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar esse ano!')
else:
    print('Já faz {} ano(s) que você deveria ter se alistado!'.format(idade - 18))
