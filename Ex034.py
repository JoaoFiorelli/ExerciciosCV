salario = float(input('Qual o valor do seu salário? '))

if (salario > 1250):
    print('Seu novo salário será de {:.2f} reais!!'.format(salario * 1.1))
else:
    print('Seu novo salário será de {:.2f} reais!!'.format(salario * 1.15))
