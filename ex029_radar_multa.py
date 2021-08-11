print('============ DESAFIO 29 / AULA 10 ============')
print('Limite de velocidade: 80Km/h')
print('Custa R$7,00 por cada Km/h acima do limite!')

velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade-80)*7
    print('Você foi multado por excesso de velocidade!')
    print('Velocidade marcada: {}km/h'.format(v))
    print('Multa refêrente a velocidade: R${:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')
