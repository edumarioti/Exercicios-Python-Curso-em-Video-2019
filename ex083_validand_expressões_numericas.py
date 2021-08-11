aula = 'DESAFIO 83 / AULA 17'
descrição = 'Validando expressões numéricas.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m')

expressão = str(input('Digite uma expressão numérica: '))
esq = expressão.count('(')
dir = expressão.count(')')
if dir == esq:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
