descrição = 'Mostra os numeros pares em certo intervalo.'
aula = 'DESAFIO 47 / AULA 13'
print('\033[1;34;m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m\n')

inicio = int(input('Informe o inicio do intervalo: '))
fim = int(input('Informe o fim do intervalo: '))
for c in range(inicio, fim, 1):
    if c % 2 == 0:
        print(c)
