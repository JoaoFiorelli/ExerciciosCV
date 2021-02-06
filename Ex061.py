a1 = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razao da PA: "))
n = 1

print("A PA será: \n")

while n <= 10:
    print(f"a{n} = {a1 + (n - 1) * razao}")
    n += 1

print("\nFIM!")
