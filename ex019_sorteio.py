print('============ DESAFIO 19 / AULA 08 ============')
print('Sorteio de Alunos\n')

from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O aluno escolhido é: {}'.format(escolhido))