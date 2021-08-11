print('============ DESAFIO 24 / AULA 08 ============')
print('Identifica se o nome da cidade tem -SANTO- no inicio\n')

city = str(input('Digite o nome de uma cidade: ')).strip()

#city = city.lower()
#city = city.split()
#v = 'santo' in city[0]
#print('O nome da cidade começa com Santo? {}'.format(v))

#modo mostrado na aula >>>
print('O nome da cidade começa com Santo? {}'.format(city[:5].upper() == 'SANTO'))
