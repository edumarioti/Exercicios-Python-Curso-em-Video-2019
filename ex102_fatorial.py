from aux_exercicios import titulo

titulo(' DESAFIO 102 / AULA 21 ',
       'Função Fatorial, com opcional de mostrar o processo.')


def fatorial(value, show=False):
    """
    :param value: número que será fatoriado.
    :param show: Opcional, mostra o processo da conta.
    :return: O valor do fatorial do numero passado.
    """
    resultado = 1
    while value > 0:
        resultado *= value
        if show:
            print(f'{value}', end='')
            print(' X ' if value > 1 else ' = ', end='')
        value -= 1
    return resultado


# Programa Principal
print(fatorial(11, show=True))
