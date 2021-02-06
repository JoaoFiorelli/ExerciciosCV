import math
catad = float(input('Digite o valor do cateto adjacente: '))
catop = float(input('Digite o valor do cateto oposto: '))

hipo = math.hypot(catad, catop)

print('A hipotenusa tem o valor: {:.2f}'.format(hipo))