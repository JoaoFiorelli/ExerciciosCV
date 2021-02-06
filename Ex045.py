import random

poss = ('pedra', 'papel', 'tesoura')

print('{:=^40}'.format('JOKENPÔ'))
print("""Suas opções são:
[1]- PEDRA
[2]- PAPEL
[3]- TESOURA""")
pessoa = int(input('Qual sua jogada? '))

if (pessoa != 1 and pessoa != 2 and pessoa != 3):
    print('Digite uma opção válida!')

PC = random.randint(1,3)

if (pessoa == 1 and PC == 3) or (pessoa == 2 and PC == 1) or (pessoa == 3 and PC == 2):
    print("""YOU WIN!!
    Você escolheu {} e eu, computador supremo, escolhi {}! :(""".format(poss[pessoa-1], poss[PC-1]))
elif (pessoa == PC):
    print("""Deu EMPATE!!
    Você escolheu {} e eu, computador supremo, escolhi {}!
    Vamos jogar de novo?""".format(poss[pessoa-1], poss[PC-1]))
elif (pessoa == 1 and PC == 2) or (pessoa == 2 and PC == 3) or (pessoa == 3 and PC == 1):
    print("""Você PERDEU!!!
    Você escolheu {} e eu, computador supremo, escolhi {}! :)""".format(poss[pessoa-1], poss[PC-1]))
