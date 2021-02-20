def ficha(jogador="<desconhecido>", gols=0):
    return f"O jogador {jogador} fez {gols} gol(s) no campeonato."


nome = input("Nome do jogador: ")
ngols = input("Número de gols: ")

if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0

if nome.strip() == "":
    print(ficha(gols=ngols))
else:
    print(ficha(nome, ngols))
