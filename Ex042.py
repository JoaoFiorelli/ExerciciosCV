l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    if (l1 == l2 == l3):
        print('Os segmentos formam um triângulo equilátero!!')
    elif (l1 != l2 != l3 != l1):
        print('Os segmentos formam um triângulo escaleno!!')
    else:
        print('Os segmentos formam um triângulo isóceles!!')
else:
    print('Os segmentos não formam um triângulo!')