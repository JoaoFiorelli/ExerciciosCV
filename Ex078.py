num = []
maior = menor = 0

for i in range(0,5):
    num.append(int(input("Digite um valor: ")))

    if i == 0:
        maior = menor = num[0]
    else:

        if num[i] > maior:
            maior = num[i]

        if num[i] < menor:
            menor = num[i]

print("\nOs números escolhidos foram: ")
print(num)
print(f"O maior valor foi o {maior} nas posições: ")

for index, valor in enumerate(num):
    if maior == valor:
        print(index + 1)

print(f"O menor valor foi o {menor} nas posicões: ")

for index, valor in enumerate(num):
    if menor == valor:
        print(index + 1)
