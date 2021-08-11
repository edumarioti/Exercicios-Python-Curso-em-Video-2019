aula = 'DESAFIO 75 / AULA 16'
descrição = 'Analisando dados de uma tupla.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

from time import sleep
numeros = (int(input('Digite um número: ')),
           int(input('Digite um segundo número: ')),
           int(input('Digite um terceiro número: ')),
           int(input('Digite um ultimo número: ')))

print('\033[34mPROCESSANDO...\033[m')
sleep(1)
print(f'Voce digitou os seguintes numeros: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {(numeros.index(3))+1}ª posição')
else:
    print(f'O valor 3 não foi digitado.')
print('Os numeros pares digitados são: ',  end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
