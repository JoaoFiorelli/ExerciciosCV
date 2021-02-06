n = (int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")))

print(f"Você digitou os valores {n}")
print(f"O número 9 foi digitado {n.count(9)} vezes!")

if 3 in n:
    print(f"O número 3 foi digitado na {n.index(3) + 1}ª posição!")
else:
    print("O número 3 não foi digitado.")

cont = 0
print("Os números pares são ", end = "")
for i in range(0,4):
    if n[i] % 2 == 0:
        print(f"{n[i]} ", end = "")
