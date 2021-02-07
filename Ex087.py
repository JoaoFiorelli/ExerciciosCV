matrix = [[], [], []]
soma = soma3 = 0

for linha in range(0,3):
    for coluna in range(0,3):

        n = int(input(f"Digite o valor da posição [{linha}][{coluna}]: "))
        matrix[linha].append(n)

        if n % 2 == 0:
            soma += n

        if coluna == 2:
            soma3 += n

        if linha == 1 and coluna == 0:
            maior2 = n
        elif linha == 1 and coluna > 0:
            if n > maior2:
                maior2 = n

print("-=" * 30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matrix[linha][coluna]:^5}]", end="")
    print()

print("-=" * 30)
print(f"A soma dos valores pares de toda a matriz é {soma}.")
print(f"A soma dos valores da coluna 3 é {soma3}.")
print(f"O maior valor da linha 2 é {maior2}.")