soma = 0

for cont in range(1,501,2):
    if cont % 3 == 0:
        soma += cont

print(f"A soma de todos os valores ímpares e multiplos de 3 entre 0 e 500 é {soma}.")
