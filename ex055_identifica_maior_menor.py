aula = 'DESAFIO 55 / AULA 13'
descrição = 'Identifica o maior e o menor peso entre os 5 informados.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso informado é: {:.1f}Kg'.format(maior))
print('E o menor peso informafo é : {:.1f}Kg'.format(menor))
