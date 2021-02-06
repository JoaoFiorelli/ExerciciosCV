while True:
    tabuada = int(input("Digite um número para fazer a tabuada [negativo encerra o programa]: "))

    if tabuada < 0:
        break

    print("-----TABUADA-----")
    n = 0

    while n <= 10:
        print(f"{n} x {tabuada} = {n * tabuada}")
        n += 1

print("FIM... Até a próxima!!")