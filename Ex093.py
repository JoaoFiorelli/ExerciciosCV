dados = {}
gols = []

dados["nome"] = input("Qual o nome do jogador? ")
npartidas = int(input(f"Quantas partidas o {dados['nome']} jogou? "))

for i in range(0, npartidas):
    gols.append(int(input(f"Quantos gols na partida {i+1}? ")))

dados["gols"] = gols[:]
dados["Total"] = sum(gols)

print("-=" * 15)
print(dados)

print("-=" * 15)
for k, v in dados.items():
    print(f"O campo {k} tem valor {v}!")

print("-=" * 15)
print(f"O jogador {dados['nome']} jogou {npartidas} partidas.")
for i, v in enumerate(gols):
    print(f"> Na partida {i+1} fez {v} gols.")
print(f"Foi um total de {dados['Total']} gols.")
