aula = ' DESAFIO 93 / AULA 19 '
descrição = 'Cadastro e desempenho de jogadores.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')

cadastro = dict()
gols = list()
cadastro['nome'] = str(input('Nome do jogador: ')).strip()
cadastro['partidas'] = int(input(f'Quantidade de partidas que {cadastro["nome"]} jogou: '))
for c in range(0, cadastro['partidas']):
    gols.append(int(input(f'Quantidade de gols na partida {c+1}: ')))
cadastro['gols'] = gols[:]
cadastro['total'] = sum(gols)
print('\033[1;34;m=' * tamanho + '\033[m')
print(f'O jogador {cadastro["nome"]} jogou {cadastro["partidas"]} partidas.')
for k, v in enumerate(cadastro['gols']):
    print(f'    => Na {k+1}º partida, fez {v} gols. ')
print(f'Somando um total de {cadastro["total"]} gols.')
