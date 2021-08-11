aula = 'DESAFIO 73 / AULA 16'
descrição = 'Analisando tabela do brasileirão.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',
          'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Ceará',
          'Botafogo', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Lista de times do Brasileirão:')
for c in range(0, len(tabela)):
    print(f'\033[1;34;m{(c+1)} -\033[m {tabela[c]}')
print('\033[1;34;m=\033[m' * 50)
print(f'Os 5 primeiros são:')
for c in range(0, 5):
    print(f'\033[1;34;m{(c + 1)} -\033[m {tabela[c]}')
print('\033[1;34;m=\033[m' * 50)
print(f'Os 4 ultimos são:')
for c in range(16, 20):
    print(f'\033[1;34;m{(c + 1)} -\033[m {tabela[c]}')
print('\033[1;34;m=\033[m' * 50)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('\033[1;34;m=\033[m' * 50)
print(f'Chapecoense está na '+f'{(tabela.index("Chapecoense")+1)}º posição')



