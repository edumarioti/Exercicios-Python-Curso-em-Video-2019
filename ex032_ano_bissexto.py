print('============ DESAFIO 32 / AULA 10 ============')
print('Calculando se um ano é bissexto\n')

import datetime # biblioteca para acessar o ano atual do sistema

ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = int(datetime.date.today().year)
    print(ano)
if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
    # Divisivel por 4
    # Divisivel por 400
    # Não divisivel por 100
    print('O ano de {} é um ano bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano bissexto.'.format(ano))
