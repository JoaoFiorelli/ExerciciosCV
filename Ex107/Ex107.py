import moeda

num = float(input("Digite o preço: R$"))
print(f"O preço {num} com um aumento de 15% é {moeda.aumentar(num, 15)}.")
print(f"O preço {num} com um desconto de 15% é {moeda.diminuir(num, 15)}.")
print(f"O dobro de {num} é {moeda.dobro(num)}.")
print(f"A metade de {num} é {moeda.metade(num)}.")