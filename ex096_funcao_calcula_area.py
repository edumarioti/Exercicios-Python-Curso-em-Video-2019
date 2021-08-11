aula = ' DESAFIO 96 / AULA 20 '
descrição = 'Função para cálculo de área'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')


def area(a, b):
    print('\033[1;34;m=' * tamanho + '\033[m')
    print(f'A área do terreno de \033[34m{a:.1f}\033[m X \033[34m{b:.1f}\033[m é de \033[34m{a * b:.1f}m²\033[m.')


area_a = float(input('Lagura: '))
area_b = float(input('Comprimento: '))
area(area_a, area_b)
