peso = 0
maior = 0
menor = 0

for pessoas in range(1,6):
    peso = float(input(f"Digite o peso da {pessoas}ª pessoa: "))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f"O maior peso foi {maior} Kg e o menor peso foi {menor} Kg!")
