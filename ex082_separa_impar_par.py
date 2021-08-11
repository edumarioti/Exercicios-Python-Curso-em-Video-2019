aula = 'DESAFIO 82 / AULA 17'
descrição = 'Cria uma lista de números pares e ímpares.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m')
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    condicao = str(input('Quer continuar? [S/N]'))[0].upper().strip()
    if condicao in 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Valores digitados: {lista}')
print(f'Valores pares: {par}')
print(f'Valores ímpares: {impar}')
