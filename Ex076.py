lista = ("Banana", 1.75,
         "Maça", 2,
         "Coco", 7.6,
         "Ameixa", 5.49,
         "Vinho", 101.5)

print("=" * 40)
print(f"{'LISTA DE COMPRAS':^40}")
print("=" * 40)

for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f"{lista[item]:.<30}", end = "")
    else:
        print(f"R$ {lista[item]:>7.2f}")

print("=" * 40)