descrição = 'Identificador de Subdivisão por Idade'
aula = 'DESAFIO 41 / AULA 12'
print('\033[34m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m')
import datetime

ano_atual = datetime.date.today().year
ano = int(input('Informe o ano de nascimento do competidor: '))
idade = ano_atual - ano
print('A idade do atleta é {} anos'.format(idade))
if idade <= 9:
    print('Você participará da categoria \033[34mMIRIM\033[m')
elif idade <= 14:
    print('Você participará da categoria \033[34mINFÂNTIL\033[m')
elif idade <= 19:
    print('Você participará da categoria \033[34mJUNIOR\033[m')
elif idade <= 20:
    print('Você participará da categoria \033[34mSÊNIOR\033[m')
else:
    print('Você participará da categoria \033[34mMASTER\033[m')