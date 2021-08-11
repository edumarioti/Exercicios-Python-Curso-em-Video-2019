print('============ DESAFIO 23 / AULA 08 ============')
print('Separando digitos de um numero\n')

n = int(input('Digite um numero entre 0 e 9999: '))
n1 = n
n = n / 10000
n = str(n)

print('Unidade: {}'.format(n[5]))
print('Dezena: {}'.format(n[4]))
print('Centena: {}'.format(n[3]))
print('Milhar: {}'.format(n[2]))

#modo mostrado na aula >>>

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10