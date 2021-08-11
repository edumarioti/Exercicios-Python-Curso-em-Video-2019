aula = 'DESAFIO 69 / AULA 15'
descrição = 'Analizando dados do grupo'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')
maior = 0
homens = 0
mulheres20 = 0
while True:
    condicao = sexo = ' '
    idade = int(input('Qual a idade? '))
    while sexo not in 'FM':
        sexo = str(input('Qual o sexo? [F/M]').upper().strip()[0])
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres20 += 1
    while condicao not in 'SN':
        condicao = str(input('Quer cadastrar outra pessoa? [S/N]').upper().strip()[0])
    if condicao == 'N':
        break
    print('='*50)
print(f'Total de pessoas com mais de 18 anos {maior}.')
print(f'Ao todo, {homens} homens foram cadastrado.')
print(f'Um total de {mulheres20} mulheres tem menos de 20 anos.')

