descrição = 'Calculadora de Indice de Massa Corporal(IMC).'
aula = 'DESAFIO 43 / AULA 12'
print('\033[34m{:=^50}'.format(aula))
print('{:^50}'.format(descrição))
print('=' * 50 + '\033[m')

altura = float(input('Informe sua altura em metros: '))
peso = float(input('Informe o seu peso: '))
imc = peso / (altura ** 2)
print('O seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade! IMC = {:.2f}'.format(imc))
else:
    print('Você está com obesidade mórbida! IMC = {:.2f}'.format(imc))
