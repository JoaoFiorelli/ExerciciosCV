n = soma = cont = maior = menor = 0
continuar = "S"

while continuar == "S":

    n = int(input("Digite um número: "))
    soma += n
    cont += 1

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
    
        if n < menor:
            menor = n

    continuar = input("Deseja continuar [S/N]? ").strip().upper()

print(f"""A média dos números é {soma / cont}. 
O maior valor é {maior}.
O menor valor é {menor}.""")