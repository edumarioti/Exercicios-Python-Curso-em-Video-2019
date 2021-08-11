aula = 'DESAFIO 85 / AULA 17'
descrição = 'Separando par e impar na lista composta.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')
num = [[], []]
for c in range(1, 8):
    dado = int(input(f'Digite o {c}º valor: '))
    if dado % 2 == 0:
        num[0].append(dado)
    else:
        num[1].append(dado)
print(f'Os números pares são: \033[1;34;m{sorted(num[0])}\033[m')
print(f'Os númeors impares são : \033[1;34;m{sorted(num[1])}\033[m')
