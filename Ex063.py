n = int(input("Quantos números da sequência de Fibonacci você deseja ver? "))
cont = 1
fn = 1
fn1 = 1

print("-----SEQUEÊNCIA DE FIBONACCI-----\n")

print("F(1) = 1")
print(f"F(2) = 1")

while cont <= n:
    fatual = fn1 + fn
    print(f"F({cont + 2}) = {fatual}")
    fn = fn1
    fn1 = fatual
    cont += 1

print("\nFim da sequência!")
