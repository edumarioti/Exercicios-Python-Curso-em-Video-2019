aula = ' DESAFIO 97 / AULA 20 '
descrição = 'Função para cálculo de área'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')


def escreva(frase):
    print('~' * (len(frase)+4))
    print(f'  {frase}')
    print('~' * (len(frase)+4))


escreva('Gustavo Guanabara')
escreva('teste')
