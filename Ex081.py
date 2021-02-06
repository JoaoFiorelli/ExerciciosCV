lista = []

while True:

    lista.append(int(input("Digite um valor: ")))

    desejo = input("Deseja continuar? [S/N]").strip().upper()[0]
    if desejo == "N":
        break

lista.sort(reverse=True)
print(f"Os números digitados foram: {lista}")
print(f"O total de números digitados foi de {len(lista)}!!")

if 5 in lista:
    print("O valor 5 se encontra na lista!")
else:
    print("O valor 5 não se encontra na lista.")
