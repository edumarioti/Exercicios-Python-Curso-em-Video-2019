descrição = 'Sistema de Condições de Pagamento.'
aula = 'DESAFIO 44 / AULA 12'
print('\033[34m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m')

valor = float(input('Informe o valor total da compra: R$'))
print("""\033[34m[ 1 ]\033[m À vista no Dinheiro/Cheque, 10% de desconto
\033[34m[ 2 ]\033[m À vista no cartão, 5%  de desconto
\033[34m[ 3 ]\033[m 2x no cartão, preço normal
\033[34m[ 4 ]\033[m 3x ou mais no cartão, 20% de juros""")
condição = int(input('Qual das opções de pagamento? '))

if condição == 1:
    total = (valor / 100) * 90
    print('Pagamento á vista no dinehiro/cheque selecionado;')

elif condição == 2:
    total = (valor / 100) * 95
    print('Pagamento á vista no cartão selecionado;')

elif condição == 3:
    total = valor
    print('Pagamento em \033[34m2x\033[m no cartão selecionado;')
    print('O valor da parcela será:  \033[34mR${}\033[m'.format(valor / 2))


elif condição == 4:
    total = (valor / 100) * 120
    parcela = int(input('Informe quantas parcelas: '))
    print('Pagamento em \033[34m{}x\033[m no cartão selecionado;'.format(parcela))
    print('O valor da parcela será: \033[34mR${}\033[m'.format((total / parcela)))
else:
    total = 0
    print('\033[31mOpção de condição invalida, por favor tente novamente!\033[m')

print('O valor final da compra fica: \033[34mR${:.2f}\033[m'.format(total))
