num = int(input("Digite um número: "))
fatorial = 1
n = num

while n != 0:
    fatorial *= n
    n -= 1

print(f"O fatorial de {num} é {fatorial}!!")