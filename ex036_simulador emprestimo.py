from time import sleep

print('\033[1;34;m============ DESAFIO 36 / AULA 12 ============')
print('           Analisandor de Emprestimo')
print('=' * 46 + '\033[m')

valor = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salario mensal: '))
anos = int(input('Em quantos anos deseja parcelar? '))

porcentagem = (salario / 100) * 30  # Calcula 30% do salario
mes = anos * 12  # Converte anos para meses
parcela = valor / mes  # Calcula o valor da parcela
print('\033[1;34;mANALIZANDO DADOS...\033[m')
sleep(2)
if parcela <= porcentagem:  # Condição para aprovação do emprestimo
    print('Parabens! Seu emprestimo foi \033[32mAPROVADO\033[m com {:} parcelas de R${:.2f}'.format(mes, parcela))
else:
    print('Desculpe, emprestimo \033[31mNEGADO\033[m, o valor da parcela é muito alto.')
    print('Por favor, reconcidere as condições de parcelamento!')
