aula = ' DESAFIO 95 / AULA 19 '
descrição = 'Cadastro e desempenho de jogadores.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')
time = list()
cadastro = dict()
gols = list()
while True:
    resposta = ' '
    cadastro['nome'] = str(input('Nome do jogador: ')).strip()
    cadastro['partidas'] = int(input(f'Quantidade de partidas que \033[1;34;m{cadastro["nome"]}\033[m jogou: '))
    for c in range(0, cadastro['partidas']):
        gols.append(int(input(f'    Quantidade de gols na partida \033[1;34;m{c + 1}\033[m: ')))
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    time.append(cadastro.copy())
    cadastro.clear()
    gols.clear()
    while resposta not in 'SN':
        resposta = str(input('Quer cadastrar outro jogador? [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break
    print('\033[1;34;m-' * tamanho + '\033[m')
print('\033[1;34;m=' * tamanho + '\033[m')
print('cod. Nome          Gols          Total')
print('\033[1;34;m-' * tamanho + '\033[m')
for k, v in enumerate(time):
    print(f'\033[1;34;m{k + 1:^4}\033[m {v["nome"]:14}{str(v["gols"]):14}{v["total"]:5}')
print('\033[1;34;m-' * tamanho + '\033[m')
print('Digite \033[33m999\033[m para sair.')
while True:
    cod = int(input('Mostrar dados de qual jogador? [Cod.]: '))
    print('\033[1;34;m-' * tamanho + '\033[m')
    if cod == 999:
        break
    if cod <= len(time):
        print(f'Detalhamento do jogador \033[1;34;m{time[cod - 1]["nome"]}\033[m')
        for k, v in enumerate(time[cod -1]['gols']):
            print(f'    -Jogo {k+1} fez {v} gols.')
        print('\033[1;34;m-' * tamanho + '\033[m')
    else:
        print(f'Erro! Não existe jogador com o cod. \033[1;34;m{cod}\033[m.')
        print('Tente novamente. ', end='')
print('Você saiu do sistema, volte sempre!')
