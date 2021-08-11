aula = 'DESAFIO 51 / AULA 13'
descrição = 'Progessão aritimetica, Imprimindo os 10 primeiros termos.'
if (len(descrição) + 6) > 50:
    a = len(descrição) + 6
else:
    a = 50
print('\033[1;34;m{:=^{}}'.format(aula, a))
print('{:^{}}'.format(descrição, a))
print('=' * a + '\033[m\n')


termo1 = int(input('Informe o primeiro termo: '))
razao = int(input('informe a razão:'))
decimo = termo1 + ((10 - 1) * razao)
for a in range(termo1, decimo + razao, razao):
    print('{}'.format(a), end = ' → ' )
print('ACABOU!')
