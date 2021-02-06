from random import randint
totalvitoria = 0

while True:

    opcao = input("Ímpar ou par? ").strip().upper()[0]

    pessoa = int(input("Digite um valor: "))
    PC = randint(0, 10)
    total = pessoa + PC
    print(f"Você escolheu {pessoa} e o computador escolheu {PC}.")

    if total % 2 == 0:
        if opcao == "P":
            print("Você escolheu PAR e ganhou!!")
            totalvitoria += 1
        elif opcao == "I":
            print("Você escolheu ÍMPAR e perdeu!!")
            break
    else:
        if opcao == "I":
            print("Você escolheu ÍMPAR e ganhou!!")
            totalvitoria += 1
        elif opcao == "P":
            print("Você escolheu PAR e perdeu!!")
            break

print(f"\nGAME OVER!! Você venceu {totalvitoria} vezes")
