print('============ DESAFIO 35 / AULA 10 ============')
print('Analisando triangulo V1.0')

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('As 3 retas pode formar um triangulo!')
else:
    print('As 3 retas não podem formar um triangulo!')

