nExtenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
            "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
            "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis",
            "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    while True:
        nEscolhido = int(input("Digite um número de 0 a 20: "))
        if 0 <= nEscolhido <=20:
            break

    print(f"O número escolhido foi o {nExtenso[nEscolhido]}")
    opcao = input("Deseja continuar [S/N]? ").strip().upper()[0]

    if opcao == "N":
        break
