palavras = ("casa", "queijo", "sapeca",
            "politica", "armazenar", "amaciante",
            "louro", "idiota", "intenso")

for p in palavras:
    print(f"\nNa palavra {p} temos as vogais ", end = "")

    for letra in p:
        if letra in "aeiou":
            print(f"{letra} ", end = "")
