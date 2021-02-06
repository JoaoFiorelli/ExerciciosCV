a1 = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razao da PA: "))
n = 1
total = 0
limite = 10

print("A PA será: \n")

while limite != 0:

    total += limite

    while n <= total:
        print(f"a{n} = {a1 + (n - 1) * razao}")
        n += 1

    print("\nPAUSA")
    limite = int(input("\nQuantos termos a mais você quer mostrar? "))

print("\nFIM!")