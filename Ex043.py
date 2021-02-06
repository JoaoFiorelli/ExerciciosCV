peso = float(input('Qual seu peso em Kg? '))
altura = float(input('Qual sua altura em metros? '))

IMC = peso / (altura ** 2)

print('Seu IMC é: {:.1f}'.format(IMC))

if (IMC < 18.5):
    print('Você está ABAIXO DO PESO!')
elif (18.5 <= IMC <25):
    print('Você está no PESO IDEAL!')
elif (25 <= IMC <30):
    print('Você está com SOBREPESO!')
elif (30 <= IMC < 40):
    print('Você está com OBESIDADE.')
elif (IMC >= 40):
    print('Você está em OBESIDADE MÓRBIDA.')
