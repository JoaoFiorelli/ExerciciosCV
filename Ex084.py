conjunto = []
pessoa = []
maior = menor = 0

while True:

    pessoa.append(input("Digite o nome da pessoa: "))
    pessoa.append(float(input("Digite o peso da pessoa: ")))

    if len(conjunto) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    conjunto.append(pessoa[:])
    pessoa.clear()

    desejo = input("Deseja continuar? [S/N]").strip().upper()[0]
    if desejo == "N":
        break

print(f"{len(conjunto)} pessoas foram cadastradas!!")
print(f"O maior peso foi {maior} das pessoas: ")

for individuo in conjunto:
    if individuo[1] == maior:
        print(individuo[0])

print(f"O menor peso foi {menor} das pessoas: ")

for individuo in conjunto:
    if individuo[1] == menor:
        print(individuo[0])

