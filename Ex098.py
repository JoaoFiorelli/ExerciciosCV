def contador(inicio, fim, passo):
    seq = []

    if passo < 0:
        passo = (-1) * passo

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            seq.append(i)

        print("-=" * 20)
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}: ")
        print(seq)
        print("-=" * 20)

    elif inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            seq.append(i)

        print("-=" * 20)
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}: ")
        print(seq)
        print("-=" * 20)


contador(1, 10, 1)
contador(10, 0, 2)

print("-=" * 20)
print("Agora é sua vez de fazer a contagem!")
inicial = int(input("Início: "))
final = int(input("Fim: "))
passo = int(input("Passo: "))
print("-=" * 20)

contador(inicial, final, passo)
