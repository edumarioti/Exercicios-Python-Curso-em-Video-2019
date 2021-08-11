aula = 'DESAFIO 88 / AULA 17'
descrição = 'Palpites da mega sena.'
if (len(descrição) + 6) > 50:
    tamanho = len(descrição) + 6
else:
    tamanho = 50
print('\033[1;34;m{:=^{}}'.format(aula, tamanho))
print('{:^{}}'.format(descrição, tamanho))
print('\033[1;34;m=' * tamanho + '\033[m')
from random import randint
from time import sleep

palpites = list()
randomico = list()
total = count = 0
jogos = int(input('Quantos palpites você quer? '))
while total < jogos:
    while True:
        num = randint(1, 60)
        if num not in randomico:
            randomico.append(num)
            count += 1
        if count >= 6:
            randomico.sort()
            palpites.append(randomico[:])
            count = 0
            randomico.clear()
            total += 1
            break
print('\033[1;34;m=' * tamanho + '\033[m')
for i, l in enumerate(palpites):
    print(f'Palpite {i + 1}: {l}')
    sleep(1)
print('Boa sorte!!!')
