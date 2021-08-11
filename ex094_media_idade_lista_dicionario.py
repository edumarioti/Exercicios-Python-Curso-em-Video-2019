aula = ' DESAFIO 94 / AULA 19 '
descrição = 'Analisa idade do grupo.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')

pessoa = dict()
grupo = list()
total = mulheres = 0
while True:
    condição = ' '
    pessoa['Nome'] = str(input('Nome: ')).strip()
    pessoa['Sexo'] = ' '
    while pessoa['Sexo'] not in 'FM':
        pessoa['Sexo'] = str(input('Sexo [M/F]: '))[0].upper().strip()
    pessoa['Idade'] = int(input('Idade: '))
    total += pessoa['Idade']
    if pessoa['Sexo'] == 'F':
        mulheres += 1
    while condição not in 'SN':
        condição = str(input('Quer continuar? [S/N]:'))[0].upper().strip()
    grupo.append(pessoa.copy())
    pessoa.clear()
    if condição in 'N':
        break
print('\033[1;34;m=' * tamanho + '\033[m')
print(f'O grupo tem \033[1;34;m{len(grupo)}\033[m pessoas.')
media = total/len(grupo)
print(f'A média de idade é \033[1;34;m{media:5.2f}\033[m anos.')
print('As mulheres cadastradas foram: ', end='')
for c in grupo:
    if c['Sexo'] in 'F':
        print(f'{c["Nome"]}', end=' ')
print()
print('Lista de pessoas que estão \033[1;34;macima\033[m da média:')
for c in grupo:
    if c['Idade'] >= media:
        print('     -', end='')
        for k, v in c.items():
            print(f' {k} = {v}', end='')
        print()
print('Encerrado...')
