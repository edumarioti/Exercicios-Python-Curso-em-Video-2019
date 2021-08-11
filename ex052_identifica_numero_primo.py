aula = 'DESAFIO 52 / AULA 13'
descrição = 'Identifica Numeros Primos.'
if (len(descrição) + 6) > 50:
    a = len(descrição) + 6
else:
    a = 50
print('\033[1;34;m{:=^{}}'.format(aula, a))
print('{:^{}}'.format(descrição, a))
print('=' * a + '\033[m\n')
n = int(input('Digite um numero: '))
a = 0
for c in range(2, 11, 1):
    s = n % c
    if s == 0 and n != c:
        a = a + 1
if c == 10 and a == 0:
    print('{} é um numero primo!'.format(n))
else:
    print('{} não é um numero primo'.format(n))

