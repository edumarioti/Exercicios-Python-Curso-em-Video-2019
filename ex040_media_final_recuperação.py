descrição = 'Sistema de Media Final'
aula = 'DESAFIO 40 / AULA 12'
print('\033[34m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m')

m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
mf = (m1 + m2)/2
if mf < 5:
    print('Sua média final é {}, você foi \033[31mREPROVADO!\033[m'.format(mf))
elif 5 <= mf < 7:
    print('Sua média final é {}, você esta em \033[32mRECUPERAÇÃO!\033[m'.format(mf))
else:
    print('Sua média final é {}, parabens, você foi \033[30mAPROVADO!\033[m'.format(mf))
