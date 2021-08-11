aula = 'DESAFIO 48 / AULA 13'
descrição = 'Impares e multiplos de três entre 1 e 500.'
print('\033[1;34;m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m\n')
soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # = soma = soma + c
        count += 1  # = count = count + 1

print('A soma de todos os {} numeros dentro dos pradões é: {}'.format(count, soma))
