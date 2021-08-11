aula = ' DESAFIO 79 / AULA 17 '
descrição = 'Lista que não permite duplicar valores'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m')
lista = list()
while True:
    valor = (int(input(f'Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar.')
    condição = str(input('Quer continuar? \033[1;34;m[S/N]\033[m')).upper().strip()
    if condição[0] in 'N':
        break
print('\033[1;34;m=' * tdd + '\033[m')
print(f'Você digitou os seguintes valores \033[1;34;m{sorted(lista)}\033[m')
