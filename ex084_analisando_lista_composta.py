aula = 'DESAFIO 84 / AULA 17'
descrição = 'Analisando dados de um cadastro.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m')
lista = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Informe o nome: ')))
    dados.append(int(input('Informe a peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    elif maior < dados[1]:
        maior = dados[1]
    elif menor > dados[1]:
        menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    condição = str(input('Quer adicionar outra pessoa? [S/N]'))[0].strip().upper()
    if condição in 'N':
        break

print('\033[1;34;m=' * tdd + '\033[m')
print(f'Ao todo você cadastrou \033[34m{len(lista)}\033[m pessoas.')
print(f'O maior peso é \033[34m{maior:.2f}Kg\033[m. Peso de: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso é \033[34m{menor:.2f}KgEd\033[m. Peso de: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

