lista = []
desejo = "S"
cont = 0

while True:
    novo = int(input("Digite um valor: "))

    if novo in lista:
        print("Não colocarei número repetidos na lista!")
    else:
        lista.append(novo)

    desejo = input("Deseja continuar? [S/N]").strip().upper()[0]
    if desejo == "N":
        break

    cont += 1

print(f"Os valores escolhidos foram: {sorted(lista)}")
