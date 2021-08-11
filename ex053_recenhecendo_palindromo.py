aula = 'DESAFIO 53 / AULA 13'
descrição = 'Frases que continuam iguais lendo ao contrário.'
if (len(descrição) + 6) > 50:
    tdd = len(descrição) + 6
else:
    tdd = 50
print('\033[1;34;m{:=^{}}'.format(aula, tdd))
print('{:^{}}'.format(descrição, tdd))
print('=' * tdd + '\033[m\n')
frase = ''.join(str(input('Digite uma frase: ')).strip().split()).upper()
tamanho = len(frase)
frase2 = frase[::-1]
a = 0
for c in range(0, tamanho, 1):
    if (frase[c]) == (frase2[c]):
        a = a + 1

if tamanho == a:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')

