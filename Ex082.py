lista = []
listapar = []
listaimpar = []

while True:

    n = int(input("Digite um valor: "))
    lista.append(n)

    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)

    desejo = input("Deseja continuar? [S/N]").strip().upper()[0]
    if desejo == "N":
        break

print(f"Os números digitados foram: {sorted(lista)}")
print(f"Os números pares são: {sorted(listapar)}")
print(f"Os números ímpares são: {sorted(listaimpar)}")
