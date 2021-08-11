aula = 'DESAFIO 87 / AULA 17'
descrição = 'Analisando matriz.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = soma3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{coluna}, {linha}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if coluna == 2:
            soma3 += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0 or maior < matriz[linha][coluna]:
                maior = matriz[linha][coluna]
print('\033[1;34;m=' * tamanho + '\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')
print('\033[1;34;m=' * tamanho + '\033[m')
print(f'A soma entre todos os valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maoir valor da segunda linha é: {maior}')

