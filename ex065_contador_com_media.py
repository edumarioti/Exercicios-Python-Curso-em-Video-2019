aula = 'DESAFIO 65 / AULA 14'
descrição = 'Contador com media'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

n = contador = soma = maior = menor = 0
continua = 'S'
while continua in 'Ss':
        n = int(input('Digite um numero:'))
        continua = str(input('Quer continuar? [S/N]').upper().strip()[0])
        soma += n
        contador += 1
        if contador == 1:
            maior = menor = n
        if maior < n:
            maior = n
        if menor > n:
            menor = n
media = soma / contador
print('Você digitou um total de \033[34m{}\033[m números'.format(contador))
print('A media entre eles é \033[34m{:2}\033[m'.format(media))
print('O maior número é \033[34m{}\033[m'.format(maior))
print('O menor número é \033[34m{}\033[m'.format(menor))
