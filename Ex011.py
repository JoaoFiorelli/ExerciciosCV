alt = float(input('Qual a altura da parede em metros? '))
larg = float(input('Qual a largura da parede em metros? '))

area = alt * larg
litros = area / 2

print('A área da parede é {} m² e será preciso {} litros de tinta para pintá-la'.format(area,litros))