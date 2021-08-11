aula = ' DESAFIO 78 / AULA 17 '
descrição = 'Identifica números e posições'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')
lista = list()
for c in range(0, 5):
    valor = int(input(f'Digite um valor para posição {c}: '))
    lista.append(valor)
    if c == 0:
       min = max = valor
    elif valor < min:
        min = valor
    elif valor > max:
        max = valor
print(f'Você digitou os seguintes números: ', end='')
for c in lista:
    print(f'{c} ', end='')
print(f'\nO maior valor digitado é {max} e está na posição: ', end='')
for p, v in enumerate(lista):
    if max == v:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado é {min} e está na posição: ', end='')
for p, v in enumerate(lista):
    if min == v:
        print(f'{p}... ', end='')
