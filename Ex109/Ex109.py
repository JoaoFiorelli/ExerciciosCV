import moeda

num = float(input("Digite o preço: R$"))
print(f"O preço {moeda.moeda(num)} com um aumento de 15% é {moeda.aumentar(num, 15, formato=True)}.")
print(f"O preço {moeda.moeda(num)} com um desconto de 15% é {moeda.diminuir(num, 15, formato=True)}.")
print(f"O dobro de {moeda.moeda(num)} é {moeda.dobro(num, formato=True)}.")
print(f"A metade de {moeda.moeda(num)} é {moeda.metade(num, formato=True)}.")