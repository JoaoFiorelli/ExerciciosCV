dados = {}
gols = []
time = []

while True:
    dados.clear()
    dados["nome"] = input("Qual o nome do jogador? ")
    npartidas = int(input(f"Quantas partidas o {dados['nome']} jogou? "))

    gols.clear()
    for i in range(0, npartidas):
        gols.append(int(input(f"Quantos gols na partida {i+1}? ")))

    dados["gols"] = gols[:]
    dados["Total"] = sum(gols)
    time.append(dados.copy())

    desejo = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if desejo == "N":
        break

print("-=" * 30)
print("Cód.", end="")
for j in dados.keys():
    print(f"{j:^15}", end="")
print()
print("-=" * 30)
for i, jogador in enumerate(time):
    print(f"{i:<5}", end="")
    for dic in jogador.values():
        print(f"{str(dic):^15}", end="")
    print()
print("-=" * 30)

while True:
    busca = int(input("Qual jogargor quer ver as informações? [999 para o programa] "))
    if busca == 999:
        break
    if busca > len(time):
        print("ERRO. Não há jogador com esse código!")
    else:
        print(f"-LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]["gols"]):
            print(f"No jogo {i+1} fez {g} gols.")
        print("-=" * 30)
