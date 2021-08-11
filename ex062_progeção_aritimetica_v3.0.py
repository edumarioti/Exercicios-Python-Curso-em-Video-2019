aula = 'DESAFIO 62 / AULA 14'
descrição = 'Progeção aritimetica v3.0'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

primeiro = int(input('Digite o primeiro número da progeção:'))
razao = int(input('Digite a razão:'))
c = 1
f = 10
print('{} → '.format(primeiro), end='')
while c < f:
    c += 1
    primeiro += razao
    print('{}'.format(primeiro), end=' → ')
    if c == f:
        print('Pausa')
        s = int(input('Quantos termos a mais você quer?'))
        f += s
print('Progeção finalizada com {} termos.'.format(f))