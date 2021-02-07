matrix = [[], [], []]

for linha in range(0,3):
    for coluna in range(0,3):

        matrix[linha].append(int(input(f"Digite o valor da posição [{linha}][{coluna}]: ")))

print("-=" * 30)

for linha in matrix:
    print(linha)
