n1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("\nTermos da PA escolhida: ")

for cont in range(1,11):
    print(n1 + (cont -1) * razao, end = " > ")
print("...")
