aula = 'DESAFIO 57 / AULA 14'
descrição = 'Lê o sexo digitado, só aceita M ou F.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
         sexo = str(input('Dados invalidos, por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
