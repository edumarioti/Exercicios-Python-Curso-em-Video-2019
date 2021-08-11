print('============ DESAFIO 31 / AULA 10 ============')
print('Preço para viagens de até 200Km: R$0.50 por Km')
print('Para viagend mais longas: R$0.45 por Km')

km = float(input('Quantos Km deseja viajar? '))
if km <= 200:
    preço = km * 0.5
else:
    preço = km * 0.45

print('O custo para uma viagem de {:.1f}Km é: R${:.2f}'.format(km, preço))
