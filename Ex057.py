sexo = input("Digite o sexo da pessoa [M/F]: ").strip().upper()

while sexo not in "MF":
    print("Sexo inválido!")
    sexo = input("Digite o sexo da pessoa [M/F]: ").strip().upper()

print("\nSexo registrado com sucesso!")