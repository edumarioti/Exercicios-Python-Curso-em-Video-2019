aula = 'DESAFIO 50 / AULA 13'
descrição = 'Soma somente os numeros pares.'
if (len(descrição) + 6) > 50:
    a = len(descrição) + 6
else:
    a = 50
print('\033[1;34;m{:=^{}}'.format(aula, a))
print('{:^{}}'.format(descrição, a))
print('=' * a + '\033[m\n')
soma = 0
count = 0
for c in range (0, 6,):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        count += 1
print('A soma final dos {} numeros pares é: \033[34m{}\033[m'.format(count, soma))
