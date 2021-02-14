def escreva(txt):
    tamanho = len(txt.strip())
    print("=" * (tamanho+4))
    print(f"  {txt:^}")
    print("=" * (tamanho + 4))


escreva(input("Digite uma frase: "))