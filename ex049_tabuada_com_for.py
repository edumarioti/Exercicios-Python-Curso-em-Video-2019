aula = 'DESAFIO 49 / AULA 13'
descrição = 'Tabuada utilizando laço for.'
a = len(descrição) + 6
print('\033[1;34;m{:=^{}}'.format(aula, a))
print('{:^{}}'.format(descrição, a))
print('=' * a + '\033[m\n')
n = int(input('Digite um numero: '))

for c in range(1, 11):
   print('{} x {:2} = {:2}'.format(n, c, (n * c)))

