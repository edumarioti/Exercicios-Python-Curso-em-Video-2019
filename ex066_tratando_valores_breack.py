aula = 'DESAFIO 66 / AULA 15'
descrição = 'Contador com condição de parada (Breack)'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

print('Para sair do sistema digite 999.')
n = contador = soma = 0
while True:
        n = int(input('Digite um numero:'))
        if n == 999:
            break
        soma += n
        contador += 1
print('Você digitou um total de \033[34m{}\033[m números'.format(contador))
print('A soma destes é \033[34m{}\033[m'.format(soma))
