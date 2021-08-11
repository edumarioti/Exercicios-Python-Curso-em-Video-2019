aula = 'DESAFIO 52 / AULA 13'
descrição = 'Identifica Numeros Primos. Forma passada em aula.'
if (len(descrição) + 6) > 50:
    a = len(descrição) + 6
else:
    a = 50
print('\033[1;34;m{:=^{}}'.format(aula, a))
print('{:^{}}'.format(descrição, a))
print('=' * a + '\033[m\n')
num = int(input('Digite um numero: '))
total = 0
for c in range (1,  num +1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi dividido {} vezes'.format(num, total))
if total >= 3:
    print('Por isso ele não é primo')
else:
    print('Por isso é primo')
