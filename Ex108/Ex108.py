import moeda

num = float(input("Digite o preço: R$"))
print(f"O preço {moeda.moeda(num)} com um aumento de 15% é {moeda.moeda(moeda.aumentar(num, 15))}.")
print(f"O preço {moeda.moeda(num)} com um desconto de 15% é {moeda.moeda(moeda.diminuir(num, 15))}.")
print(f"O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}.")
print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}.")