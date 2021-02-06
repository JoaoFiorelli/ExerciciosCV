n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
opcao = 0

while opcao != 5:
    print("""Qual das opções a seguir você deseja realizar? 
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior valor
    [4] - Novos números
    [5] - Sair do programa""")
    opcao = int(input("Escolha: "))

    if opcao == 1:
        print(f"A soma dos números é {n1 + n2}!!")
    elif opcao == 2:
        print(f"A multiplicação dos números é {n1 * n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}!!")
        else:
            print(f"{n2} é maior que {n1}!!")
    elif opcao == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Digite uma opção válida.")

print("Fim do programa!!!")