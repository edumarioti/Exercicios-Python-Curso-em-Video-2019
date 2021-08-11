print('============ DESAFIO 26 / AULA 08 ============')
print('Identifica letras |A| na frase desejada\n')

frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra |A| aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra |A| está na posição {}'.format(frase.find('a')+1))
print('A ultima letra |A| está na posição {}'.format(frase.rfind('a')+1))
