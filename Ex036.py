valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))

prestacao = valor / (anos * 12)

if (prestacao > (0.3 * salario)):
    print('O valor da prestação seria de {:.2f} reais e seu empréstimo foi NEGADO!!'.format(prestacao))
else:
    print("Empréstimo aceito! O Valor mensal a ser pago será de {:.2f} reais.".format(prestacao))
