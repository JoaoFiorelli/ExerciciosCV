valores = [[], []]

for i in range(0,7):

    n = int(input(f"Digite o {i + 1}º valor: "))

    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print(f"Os valores pares são: {sorted(valores[0])}")
print(f"Os valores ímpares são: {sorted(valores[1])}")
