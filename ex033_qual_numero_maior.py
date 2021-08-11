print('============ DESAFIO 33 / AULA 10 ============')
print('Informe três numeros e lhe direi qual é o maoir e o menor')

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
# Verifica quem é menor
menor = a  # diminui uma verificação (if)
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verifica quem é maior
maior = a  # diminui uma verificação (if)
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {} e o maoir é {}'.format(menor, maior))
