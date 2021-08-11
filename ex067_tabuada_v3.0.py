aula = 'DESAFIO 67 / AULA 15'
descrição = 'Tabuada v3.0 (Breack)'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

while True:
    n = int(input('Quer ver a tabuada de que valor?'))
    if n < 1:
        break
    print('\033[34m=\033[m'*50)
    print(f'Tabuada do \033[34m{n}\033[m')
    for c in range(1, 11):
        print(f'\033[34m{n:2}\033[m x \033[34m{c:2}\033[m = \033[34m{(n*c):2}\033[m')
    print('\033[34m=\033[m' * 50)
print('\033[34m=\033[m' * 50)
print('PROGRAMA DE TABUADA ENCERRADO!')