print('\033[34m============ DESAFIO 36 / AULA 12 ============')
print('    Conversor de decimal para bi/hex/oct')
print('=' * 46 + '\033[m')


valor = int(input('Digite o valor a ser convertido: '))
print("""\033[34m[ 1 ]\033[m BINÁRIO
\033[34m[ 2 ]\033[m OCTAL
\033[34m[ 3 ]\033[m HEXADECIMAL""")
base = int(input('Escolha uma das opções: '))

if base == 1:
    print('O valor {} em base \033[34mBINÁRIA\033[m fica \033[34m{}\033[m'.format(valor, bin(valor)[2:]))
elif base == 2:
    print('O valor {} em base \033[34mOCTAL\033[m fica \033[34m{}\033[m'.format(valor, oct(valor)[2:]))
elif base == 3:
    print('O valor {} em base \033[34mHEXADECIMAL\033[m fica \033[34m{}\033[m'.format(valor, hex(valor)[2:]))
else:
    print('\033[31mOpção de base invalida! Tente novamente.\033[m')

