aula = 'DESAFIO 72 / AULA 16'
descrição = 'Número por extenso.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quize', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero < 21:
        break
    print('Tente novamente! ', end='')
print(f'Você digitou o número \033[34m{extenso[numero]}!\033[m')
