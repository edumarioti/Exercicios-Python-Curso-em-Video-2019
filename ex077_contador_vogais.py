aula = 'DESAFIO 77 / AULA 16'
descrição = 'Contador de vogais.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico-PR', 'Sao Paulo', 'Internacional',
          'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco', 'Atletico-MG', 'Fluminense', 'Ceara',
          'Botafogo', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')
for c in tabela:
    print(f'\nNa palavra \033[1;34;m{c}\033[m temos estas vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')