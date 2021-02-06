#####################################
# OUTRA FORMA DE REALIZAR O JOKENPÔ #
#####################################

import random

PEDRA = 'pedra'
PAPEL = 'papel'
TESOURA = 'tesoura'

possibilidades = (PEDRA, PAPEL, TESOURA)

print('{:=^40}'.format('JOKENPÔ'))
print("""Suas opções são:
[1]- PEDRA
[2]- PAPEL
[3]- TESOURA""")
pessoa = input('Qual sua jogada? ')
pessoa = pessoa.strip().lower()

if pessoa not in possibilidades:
    print('Digite uma opção válida!')

PC = possibilidades[random.randint(0,2)]

mensagens = {
    'empate':'Deu empate',
    'vitoria':'YOU WIN!!',
    'derrota':'Perdedor! :)',
}

resultado = {
    'pedra-pedra': mensagens['empate'],
    'pedra-tesoura': mensagens['vitoria'],
    'pedra-papel': mensagens['derrota'],
    'tesoura-pedra': mensagens['derrota'],
    'tesoura-tesoura': mensagens['empate'],
    'tesoura-papel': mensagens['vitoria'],
    'papel-pedra': mensagens['vitoria'],
    'papel-tesoura': mensagens['derrota'],
    'papel-papel': mensagens['empate'],
}

chave = f'{pessoa}-{PC}'
print("-=" * 32)
print(resultado[chave])
print(f"Você escolheu {pessoa} e eu, computador supremo, escolhi {PC}!")
print("-=" * 32)


