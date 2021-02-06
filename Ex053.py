frase = input("Digite uma frase: ").strip().lower().replace(" ","")
fraseinv = frase[::-1]
if frase == fraseinv:
    print("A frase figitada é um palíndromo!!")
else:
    print("A frase digitada não é um palíndromo.")
