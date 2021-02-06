expressao = input("Digite a expressão desejada: ")
pilha = []

for letra in expressao:

    if letra == "(":
        pilha.append("(")
    elif letra == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("A expressão é válida!!")
else:
    print("A expressão não é válida.")
