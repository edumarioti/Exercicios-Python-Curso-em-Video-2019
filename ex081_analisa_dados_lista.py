aula = 'DESAFIO 81 / AULA 17'
descrição = 'Extrai dados da lista de números.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m')
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    condicao = str(input('Quer continuar? [S/N]'))[0].upper().strip()
    if condicao in 'N':
        break
print('\033[1;34;m=' * tdd + '\033[m')
print(f'O total de números digitados é: \033[1;34;m{len(lista)}\033[m')
print(f'A lista em ordem decrescente é: \033[1;34;m{sorted(lista, reverse=True )}\033[m')
if 5 in lista:
    print('O valor 5 está presente na lista!')
else:
    print('O valor 5 não está presente a lista.')
