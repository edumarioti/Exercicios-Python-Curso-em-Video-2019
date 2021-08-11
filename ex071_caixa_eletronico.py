aula = 'DESAFIO 71 / AULA 15'
descrição = 'Caixa Eltrônico Python'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

totalced = 0
nota = 100
valor = int(input('Digite quanto você deseja sacar. R$:'))
print('\033[34m=\033[m' * 50)
print('Total de cédulas:')
total = valor
while True:
    if total >= nota:
        total -= nota
        totalced += 1
    else:
        if totalced > 0:
            print(f'\033[34m{totalced}\033[m notas de R${nota}')
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        totalced = 0
        if total == 0 or total == 1:
            break
if total == 0:
    print('\033[34m=\033[m' * 50)
    print('Obrigado pela preferência! Tenha um bom dia.')
