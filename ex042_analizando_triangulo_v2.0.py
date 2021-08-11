descrição = 'Analizando Triangulo e Identificando o mesmo.'
aula = 'DESAFIO 42 / AULA 12'
print('\033[34m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m')

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('\nAs 3 retas pode formar um triangulo!')
    if a == b == c:
        print('O triangulo formado é um \033[36mEQUILÁTERO;\033[m\nOu seja, tem todos os lados iguais.')
    elif a == b or b == c or a == c:
        print('O triangulo formado é um \033[36mISÓSCELES;\033[m\nOu seja, tem dois lados iguais.')
    else:
        print('O triangulo formado é um \033[36mESCALENO;\033[m\nOu seja, tem todos os lados diferentes.')
else:
    print('As 3 retas não podem formar um triangulo!')



