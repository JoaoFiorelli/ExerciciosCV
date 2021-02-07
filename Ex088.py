from random import randint
from time import sleep

print("-=" * 30)
print(f"{'JOGO NA MEGA SENA':^60}")
print("-=" * 30)

jogadas = int(input("Quantos jogos você quer que eu sorteie? "))
jogo = []
jogototal = []

for j in range(0, jogadas):
    for n in range(0,6):

        while True:
            sorteio = randint(1, 60)
            if sorteio not in jogo:
                break

        jogo.append(sorteio)

    jogototal.append(jogo[:])
    jogo.clear()

    sleep(1)
    print(f"Jogo {j + 1}: {sorted(jogototal[j])}")

print(f"{' BOA SORTE ':=^60}")
