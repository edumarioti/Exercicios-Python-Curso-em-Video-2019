from aux_exercicios import titulo

def voto(ano=0):
    global frase
    from datetime import datetime
    if ano != 0:
        atual = datetime.today().year
        idade = atual - ano
        if idade < 16:
            return f'Com {idade} anos: NÃO VOTA.'
        elif 16 <= idade < 18 or idade > 65:
            return f'Com {idade} anos: VOTO OPCIONAL.'
        else:
            return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Cabeçalho:
titulo(' DESAFIO 101 / AULA 20 ',
       'Identifica quem necessita votar.')

# Programa principal
data = voto(int(input('Em que ano você nasceu? ')))
print(data)

