print('============ DESAFIO 04 / AULA 06 ============ ')

a = input('Digite algo: ')
print('Variavel do tipo:', type(a))
print('Só tem espaços', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumerérico?', a.isalnum())
print('Esta em letra maiuscula?', a.isupper())
print('Esta em letra minuscula?', a.islower())
print('Esta capitalizada?', a.istitle())