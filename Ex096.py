def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área do terreno de dimensões {largura:.2f} m x {comprimento:.2f} m é de {area:.2f} m².")


print("CONTROLE DE TERRENOS:")
print("-=" * 15)
tamanho1 = float(input("Largura[m]: "))
tamanho2 = float(input("Comprimento[m]: "))
area(tamanho1, tamanho2)