somaidade = 0
contmulher = 0
velho = 0

for pessoa in range(1,5):
    print(f"----------{pessoa}ª PESSOA----------")
    nome = input(f"Qual o nome da {pessoa}ª pessoa? ").strip()
    idade = int(input(f"Qual a idade da {pessoa}ª pessoa? "))
    sexo = input("Digite M se é do sexo masculino e F se é do feminino: ").strip().upper()

    somaidade += idade

    if sexo == "M" and idade > velho:
        velho = idade
        nomevelho = nome

    if sexo == "F" and idade < 20:
        contmulher += 1

print(f"\nA média de idade das pessoas é de {somaidade/4} anos.")
print(f"O nome do homem mais velho é {nomevelho}, tendo {velho} anos!")
print(f"O número de mulheres abaixo dos 20 anos é de {contmulher}!!")