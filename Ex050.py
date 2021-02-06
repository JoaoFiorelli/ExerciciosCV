soma = 0
for cont in range(0,6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n
print(f"O valor da soma dos número pares é {soma}!!")