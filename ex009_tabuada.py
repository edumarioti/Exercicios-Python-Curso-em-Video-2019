print('============ DESAFIO 09 / AULA 07 ============ ')

n = int(input('Digite um numero: '))

n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10

print('\n-----------\n{} x  1 = {}\n{} x  2 = {}\n{} x  3 = {}\n{} x  4 = {}\n{} x  5 = {}\n'.format(n, n, n, n2, n, n3, n, n4, n, n5), end='')
print('{} x  6 = {}\n{} x  7 = {}\n{} x  8 = {}\n{} x  9 = {}\n{} x 10 = {}\n-----------\n'.format(n, n6, n, n7, n, n8, n, n9, n, n10))

# ou melhor:

print('-'*11)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-'*11)