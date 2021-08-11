print('\033[34m============ DESAFIO 38 / AULA 12 ============')
print(' Analiza qual o numero maior ou se são iguais')
print('=' * 46 + '\033[m')

primeiro = float(input('Informe o primeiro numero: '))
segundo = float(input('Informe o segundo numero: '))
if primeiro > segundo:
    print('O \033[34mPRIMEIRO\033[m valor é maior')
elif segundo > primeiro:
    print('O \033[34mSEGUNDO\033[m valor é maior')
else:
    print('Os valores são \033[34mIGUAIS\033[m!')