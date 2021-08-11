aula = ' DESAFIO 89 / AULA 17 '
descrição = 'Sistema de boletim.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')
lista = list()
nomes = list()
notas = list()
sel = 0
while True:
    nomes.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Digite a nota 1: ')))
    notas.append(float(input('Digite a nota 2: ')))
    notas.append((notas[0]+notas[1])/2)
    nomes.append(notas[:])
    lista.append(nomes[:])
    notas.clear()
    nomes.clear()
    condição = str(input('Quer cadastrar outro aluno? [S/N] '))[0].upper().strip()
    if condição in 'N':
        break
print('\033[1;34;m=' * tamanho + '\033[m')
print('\033[1;34;mNº    Nome        Média\033[m')
print('\033[1;34;m-' * 23 + '\033[m')
for c in range(len(lista)):
    print(f'\033[1;34;m{c + 1}\033[m     {lista[c][0]:10}{lista[c][1][2]:7}')
print('\033[1;34;m=' * tamanho + '\033[m')
while sel != 999:
    print('Digite o valor \033[32m 999\033[m para sair do programa. ')
    sel = int(input('Digite o numero no aluno o qual deseja ver as notas: '))
    if sel == 999:
        break
    print('\033[1;34;m=' * tamanho + '\033[m')
    print(f'As notas de {lista[sel-1][0]} são: '
          f'\033[1;34;m{lista[sel-1][1][0]:.1f}\033[m e \033[1;34;m{lista[sel-1][1][1]:.1f}\033[m')
    print('\033[1;34;m=' * tamanho + '\033[m')
print('\033[1;34;m=' * tamanho + '\033[m')
print('Programa encerrado, obrigado por utilizar nosso sistema!')