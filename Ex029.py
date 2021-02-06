vel = float(input('Qual a velocidade do carro em Km/h? '))

if vel <= 80:
    print('Parabéns, você não foi multado!')
else:
    print('Você foi multado e deverá pagar {:.2f} reais de multa!'.format((vel - 80) * 7))