l1 = float(input('Digite o tamanho do primeiro segmento de reta: '))
l2 = float(input('Digite o tamanho do segundo segmento de reta: '))
l3 = float(input('Digite o tamanho do terceiro segmento de reta: '))

if (l1 + l2 > l3):
    if (l1 + l3 > l2):
        if (l2 + l3 > l1):
            print('É possível fazer um triângulo com esses segmentos de reta!!')
        else:
            print('Não é possível fazer um triângulo.')
    else:
        print('Não é possível fazer um triângulo.')
else:
    print('Não é possível fazer um triângulo.')
