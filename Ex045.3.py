######################################################
# VERSÃO DE JOKEPÔ Pedra-papel-tesoura-lagarto-Spock #
######################################################

############### REGRAS ###############
#                                    #
# Tesoura corta papel                #
# Papel cobre pedra                  #
# Pedra esmaga lagarto               #
# Lagarto envenena Spock             #
# Spock esmaga (ou derrete) tesoura  #
# Tesoura decapita lagarto           #
# Lagarto come papel                 #
# Papel refuta Spock                 #
# Spock vaporiza pedra               #
# Pedra amassa tesoura               #
#                                    #
######################################

import random

PEDRA = 'pedra'
PAPEL = 'papel'
TESOURA = 'tesoura'
LAGARTO = 'lagarto'
SPOCK = 'spock'

possibilidades = (PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK)

print('{:=^40}'.format('JOKENPÔ'))
print("""Suas opções são:
[1]- PEDRA
[2]- PAPEL
[3]- TESOURA
[4]- LAGARTO
[5]- SPOCK""")
pessoa = input('Qual sua jogada? ')
pessoa = pessoa.strip().lower()

if pessoa not in possibilidades:
    print('Digite uma opção válida!')

PC = possibilidades[random.randint(0,4)]

mensagem = {
    'empate': 'Empatou.',
    'derrota': 'Você perdeu!! :)',
    'vitoria': 'YOU WIN!!',
}

resultado = {
    'pedra-pedra': mensagem['empate'],
    'pedra-papel': mensagem['derrota'],
    'pedra-tesoura': mensagem['vitoria'],
    'pedra-lagarto': mensagem['vitoria'],
    'pedra-spock': mensagem['derrota'],
    'papel-pedra': mensagem['vitoria'],
    'papel-papel': mensagem['empate'],
    'papel-tesoura': mensagem['derrota'],
    'papel-lagarto': mensagem['derrota'],
    'papel-spock': mensagem['vitoria'],
    'tesoura-pedra': mensagem['derrota'],
    'tesoura-papel': mensagem['vitoria'],
    'tesoura-tesoura': mensagem['empate'],
    'tesoura-lagarto': mensagem['vitoria'],
    'tesoura-spock': mensagem['derrota'],
    'lagarto-pedra': mensagem['derrota'],
    'lagarto-papel': mensagem['vitoria'],
    'lagarto-tesoura': mensagem['derrota'],
    'lagarto-lagarto': mensagem['empate'],
    'lagarto-spock': mensagem['vitoria'],
    'spock-pedra': mensagem['vitoria'],
    'spock-papel': mensagem['derrota'],
    'spock-tesoura': mensagem['vitoria'],
    'spock-lagarto': mensagem['derrota'],
    'spock-spock': mensagem['empate'],
}

chave = f"{pessoa}-{PC}"
print("-=" * 32)
print(resultado[chave])
print(f"Você escolheu {pessoa.upper()} e eu, computador supremo, escolhi {PC.upper()}!")
print("-=" * 32)
