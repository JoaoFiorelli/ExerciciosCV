n = int(input('Digite o número inteiro a ser convertido: '))
print('''Qual será a base para a qual ele será convertido?
Digite:
1- Binário
2- Octal
3- Hexadecimal''')
base = int(input('Qual sua escolha? '))

if (base == 1):
    print('O valor {} em base binária é {}!'.format(n, bin(n)[2:]))
elif (base == 2):
    print('O valor {} em base octal é {}!'.format(n, oct(n)[2:]))
elif (base == 3):
    print('O valor {} em base hexadecimal é {}!'.format(n, hex(n)[2:]))
else:
    print('Escolha uma opção válida de base para a conversão!')
