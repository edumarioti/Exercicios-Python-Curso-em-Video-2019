from aux_exercicios import titulo

titulo(' DESAFIO 103 / AULA 21 ',
       'Função Ficha, com prenchimento caso vazio.')


def ficha(name="<desconhecido>", gols=0):
    print(f'O jogador {name} fez \033[1;34;m{gols}\033[m gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gol = str(input('Quantidade de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)

