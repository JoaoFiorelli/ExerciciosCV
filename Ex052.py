n = int(input("Digite um número: "))
soma = 0

for cont in range(1,n+1):

    if n % cont == 0:
        soma += 1

if soma == 2:
    print(f"O número {n} é primo!")
else:
    print(f"O número {n} não é primo.")
