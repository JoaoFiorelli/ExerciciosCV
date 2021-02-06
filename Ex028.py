import random
n = int(input('Digite um número de 0 a 5 para tentar adivinhar qual o computador escolheu: '))
if n == random.randint(0,5):
    print('PARABÉNS!! Você acertou!!')
else:
    print('Sorry, você errou. :(')
