aula = 'DESAFIO 76 / AULA 16'
descrição = 'Listagem de preços.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

tupla = ('Pão', 1, 'Café', 2.50, 'Nescal', 4.99, 'Pão de queijo', 5.50)
for c in range(0, len(tupla), 2):
    print(f'{tupla[c]:.<20}R$:{tupla[c+1]:>5.2f}')
print('\033[1;34;m=' * tdd + '\033[m\n')
