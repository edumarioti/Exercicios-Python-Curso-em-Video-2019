aula = 'DESAFIO 60 / AULA 14'
descrição = 'Fatorial!'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

n = int(input('Utilizando \033[34mWHILE\033[m\nDigite um número:'))
r = 1
t = n
print('{}! = '.format(n), end='')
while n != 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    r = r * n
    n -= 1
print('\033[34m{}\033[m'.format(r))

