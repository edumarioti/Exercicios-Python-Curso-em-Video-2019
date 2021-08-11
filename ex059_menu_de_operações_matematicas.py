aula = 'DESAFIO 59 / AULA 14'
descrição = 'Menu de operações matetematicas.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')

from time import sleep

menu = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while menu != 5:
    menu = int(input('Escolha uma das opções:\n\033[34m[1]\033[m Somar\n\033[34m[2]\033[m Multiplicar\n\033[34m'
                     '[3]\033[m Maior\n\033[34m[4]\033[m Novos Números\n\033[34m[5]\033[m Sair do programa\n'))
    if menu == 1:
        print('A soma entre \033[34m{}\033[m e \033[34m{}\033[m é \033[34m{}\033[m.'.format(n1, n2, (n1 + n2)))
    elif menu == 2:
        print('A multiplicação entre \033[34m{}\033[m e \033[34m{}\033[m é \033[34m{}\033[m.'.format(n1, n2, (n1 * n2)))
    elif menu == 3:
        if n1 > n2:
            print('O numero \033[34m{}\033[m é maior que o número \033[34m{}\033[m.'.format(n1, n2))
        elif n2 > n1:
            print('O numero \033[34m{}\033[m é maior que o número \033[34m{}\033[m.'.format(n2, n1))
        else:
            print('Os números são iguais!')
    elif menu == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif menu == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('\n\033[31mNúmero invalido! tente novamente\033[m')
    print('\033[34m=\033[m' * 50)
print('\033[34mObrigado por utlizar nosso sistema!!!\033[m')
