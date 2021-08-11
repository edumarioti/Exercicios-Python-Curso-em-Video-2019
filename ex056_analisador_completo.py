aula = 'DESAFIO 56 / AULA 13'
descrição = 'Analisa 4 pessoas e faz suas conclusões.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')
media = 0
maior = 0
count = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).split()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().split()
    media += idade
    if sexo == ['M']:
        if idade > maior:
            maior = idade
            nomemaior = nome
    else:
        if idade < 20:
            count += 1
print('A média de idade do grupo é {:.1f} anos'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomemaior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(count))




