print("=" * 30)
print("BANCO TESTINHO")
print("=" * 30)

valor = int(input("\nDigite o valor a ser sacado: R$"))
cedula = 50
quantcedula = 0

while True:
    if valor >= cedula:
        valor -= cedula
        quantcedula += 1
    else:
        if quantcedula > 0:
            print(f"Total de {quantcedula} cédulas de R${cedula}")

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        quantcedula = 0

        if valor == 0:
            break

print("=" * 30)
print("Voltei sempre!")