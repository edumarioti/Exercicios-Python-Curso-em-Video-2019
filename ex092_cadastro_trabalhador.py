aula = ' DESAFIO 92 / AULA 19 '
descrição = 'Cadastro de trabalhadores.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')

from datetime import datetime

cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).strip()
cadastro['Idade'] = datetime.now().year - int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Nº Carteira de trabalho (Digite 0 caso não tenha): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (35 - (datetime.now().year - cadastro['Contratação']))
    cadastro['Salário'] = float(input('Salário: R$ '))
print('\033[1;34;m=' * tamanho + '\033[m')
for k, v in cadastro.items():
    print(f'    - {k} tem o valor {v}')
