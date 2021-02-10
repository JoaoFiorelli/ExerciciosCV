from random import randint
from operator import itemgetter

dados = {}
ranking = []

for i in range(0,4):
    dados[f"jogador{i+1}"] = randint(1,6)

for k, v in dados.items():
    print(f"{k} tirou {v} no dado!")

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print("-=" * 15)
print("== RANKING DOS JOGADORES ==")

for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}!")