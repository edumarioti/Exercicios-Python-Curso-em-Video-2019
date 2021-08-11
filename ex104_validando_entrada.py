def título(aula, descrição):
    """
    Cabeçaalho de projetos.
    :param aula: Título
    :param descrição: Subtítulo
    """
    if (len(descrição) + 6) > 50:
        tamanho = len(descrição) + 6
    else:
        tamanho = 50
    print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
    print('{:^{}}'.format(descrição, tamanho))
    print('\033[1;34;m=' * tamanho + '\033[m')


def linha():
    """
    Cria uma linha divisória para melhor visualização.
    """
    print('\033[1;34;m=\033[m' * 50)


# Cabeçalho:
título(' DESAFIO 104 / AULA 21 ',
       'Função LeiaInt, só permite números inteiros como entrada.')


def LeiaInt(msg):
    """
    Valida a entrada de números inteiros.
    :param msg: mensagem que será visualizada para entrada do valor
    :return: valor inteiro digitado
    """
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mERRO! Digite um valor númerico inteiro.\033[m')
    return num


n = LeiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')