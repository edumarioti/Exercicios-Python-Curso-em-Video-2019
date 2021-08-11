aula = 'DESAFIO 70 / AULA 15'
descrição = 'Super mercado Python'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

total = mil = valorb = 0
produtob = ' '
while True:
    condicao = ' '
    produto = str(input('Nome de produto: '))
    valor = float(input('Preço do produto: '))
    total += valor
    if valor >= 1000:
        mil += 1
    if valorb > valor or valorb == 0:
        valorb = valor
        produtob = produto
    while condicao not in 'SN':
        condicao = str(input('Quer continuar? [S/N]').upper().strip()[0])
    if condicao == 'N':
        break
    print('=' * 50)
print(f'\nO valor total da compra é {total}.')
print(f'Há {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato é {produtob}, custando {valorb:.2f}')
