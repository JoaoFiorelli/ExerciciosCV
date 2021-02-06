dist = float(input('Qual a distância a ser percorrida na viagem, em Km? '))

if (dist <= 200):
    print('O preço para essa viagem será de {:.2f} reais!'.format(dist * 0.5))
else:
    print('O preço para essa viagem será de {:.2f} reais!'.format(dist * 0.45))
