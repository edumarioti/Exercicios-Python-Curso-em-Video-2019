
TAMANHO_PADRAO_CABECALHO = 60

AUMENTO_DO_TAMANHO = 10 


def titulo(titulo, subtitulo=''):
    '''
    Cabeçalho para os execícios do curso.
    '''

    tamanho_cabecalho = len(subtitulo)

    if tamanho_cabecalho > TAMANHO_PADRAO_CABECALHO:
        tamanho_cabecalho += AUMENTO_DO_TAMANHO
    else:
        tamanho_cabecalho = TAMANHO_PADRAO_CABECALHO

 
    print(f'{titulo:=^{tamanho_cabecalho}}')

    if subtitulo != '':
        print(f'{subtitulo:^{tamanho_cabecalho}}')
        print(f'=' * tamanho_cabecalho)


def linha(tamanho=TAMANHO_PADRAO_CABECALHO):
    '''
    Cria uma linha divisória para melhor visualização.
    '''
    print('=' * tamanho)

