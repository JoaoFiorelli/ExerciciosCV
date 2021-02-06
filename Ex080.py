lista = []

for i in range(0,5):
    n = int(input("Digite um número: "))

    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1

print("=" * 30)
print(f"Os valores em ordem são: {lista}")
