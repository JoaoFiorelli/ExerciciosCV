cont = soma = 0

while True:

    n = int(input("Digite um número [999 encerra o programa]: "))

    if n == 999:
        break

    cont += 1
    soma += n

print(f"O total de número digitados foi {cont} e a soma deles é {soma}!!")