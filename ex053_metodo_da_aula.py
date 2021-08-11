aula = 'DESAFIO 53 / AULA 13'
descrição = 'Frases que continuam iguais lendo ao contrário. Metodo explicado na aula.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    a = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

'''inverso = ''
for letra in range(len(junto)- 1, -1, -1):
    inverso += junto[letra] '''

inverso = junto[::-1]  # macete do python!!!

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')
