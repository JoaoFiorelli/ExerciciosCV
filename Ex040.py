n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/ 2

if (media < 5):
    print('Sua média é {:.1f} e você está REPROVADO.'.format(media))
elif (5 <= media < 7):
    print('Sua média é {:.1f} e você está de RECUPERAÇÂO.'.format(media))
elif (media >= 7):
    print('Sua média é {:.1f} e você está APROVADO!!! Parabéns!!'.format(media))
