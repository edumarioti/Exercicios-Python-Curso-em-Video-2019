print('============ DESAFIO 22 / AULA 08 ============')
print('Manipulando um Nome\n')

nome = str(input('Escreva seu nome completo:'))
nome1 = nome
print('Analizando seu nome...')
print('Maiusculo: {}'.format(nome.upper()))
print('minusculo: {}'.format(nome.lower()))

nome = nome.split()
print('A quantidade de letras no primeiro nome é: {}'.format(len(nome[0])))

nome = ''.join(nome)
print('A quantidade de letras no nome completo é: {}'.format(len(nome)))

# modo demonstrado no video >>>

print('A quantidade de letras no primeiro nome é: {}'.format(len(nome1) - nome1.count(' ')))
print('A quantidade de letras no nome completo é: {}'.format(nome1.find(' ')))
