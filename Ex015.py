dias = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Qual a distância percorrida em Km? '))

preco = (60 * dias) + (0.15 * km)

print('O preço a ser pago pelo aluguel do carro é de {:.2f} reais!'.format(preco))