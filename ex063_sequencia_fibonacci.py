aula = 'DESAFIO 63 / AULA 14'
descrição = 'Sequencia de Fibonacci'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')


termos = int(input('Quantos termos você deseja na sequencia?'))
t1 = 0
t2 = 1
c = 2
print('{} → {} → '.format(t1, t2), end='')
while c != termos:
    t3 = t1 + t2
    print('{}'.format(t3), end=' → ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
