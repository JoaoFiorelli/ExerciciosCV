total = precomaior = cont = menor = 0
nomebarato = ""

while True:

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))

    total += preco

    if preco > 1000:
        precomaior += 1

    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomebarato = nome

    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja continuar cadastrando [S/N]? ").strip().upper()[0]

    if opcao == "N":
        break

print(f"""\nO total da compra foi {total:.2f} reais!
{precomaior} produtos custam mais que 1000 reais!
O produto mais barato é o {nomebarato} custando {menor:.2f} reais""")
