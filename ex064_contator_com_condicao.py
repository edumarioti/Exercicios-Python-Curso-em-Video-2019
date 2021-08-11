aula = 'DESAFIO 64 / AULA 14'
descrição = 'Contador com condição de parada'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

print('Para sair do sistema digite 999.')
n = contador = soma = 0
n = int(input('Digite um numero:'))
while n != 999:
        soma += n
        contador += 1
        n = int(input('Digite um numero:'))
print('Você digitou um total de \033[34m{}\033[m números'.format(contador))
print('A soma destes é \033[34m{}\033[m'.format(soma))
