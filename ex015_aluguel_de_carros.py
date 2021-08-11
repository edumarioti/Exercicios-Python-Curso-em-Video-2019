print('============ DESAFIO 15 / AULA 07 ============ ')

km = float(input('Quantos Km rodados? '))
d = float(input('Quantos dias alugados? '))

total = (km*0.150)+(d*60)

print('O valor a ser pago é R$:{:.2f}'.format(total))
