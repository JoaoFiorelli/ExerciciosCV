print('{:=^40}'.format('CALCULADORA DE PRESTAÇÃO'))

preco = float(input('Qual o valor do produto? R$'))
print("""Qual a forma de pagamento?
[1]- Dinheiro/Cheque
[2]- Cartão de crédito""")
metodo = int(input('Digite: '))

if (metodo == 2):
    parc = int(input('Qual o número de parcelas? '))
elif (1 != metodo != 2 ):
    print('Digite uma opção válida!')

if (metodo == 1):
    print('O valor do produto será {:.2f} reais!'.format(0.9 * preco))
elif (metodo == 2 and parc == 1):
    print('O valor do produto será de {:.2f} reais!'.format(0.95 * preco))
elif (metodo == 2 and parc == 2):
    print('O valor do produto será {:.2f} reais, em duas parcelas de {:.2f} reais!'.format(preco, preco/2))
elif (metodo == 2 and parc >= 3):
    print('O valor do produto será de {:.2f} reais, em {} parcelas de {:.2f} reais!'.format(1.2 * preco, parc, (1.2 * preco)/parc))
