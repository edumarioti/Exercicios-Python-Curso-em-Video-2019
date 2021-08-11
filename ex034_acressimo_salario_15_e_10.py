print('============ DESAFIO 34 / AULA 10 ============')
print('Acressimo de 15% para salarios abaixo de R$1250,00')
print('Acressimo de 10% para salarios acima de R$1250,00')

salario = float(input('Informe o salario atual: '))
if salario <= 1250:
    novo = (salario / 100) * 115
else:
    novo = (salario / 100) * 110

print('Seu salario de R$:{:.2f} passa a ser R${:.2f} com o reajuste'.format(salario, novo))
