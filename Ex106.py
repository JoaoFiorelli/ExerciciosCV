def ajuda(name):
    info = help(name)
    return info

def titulo(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


titulo("Ajuda Python")

while True:
    comando = input("Digite o comando: ").strip().lower()
    if comando == "fim":
        break
    titulo(comando.upper())
    print(ajuda(comando))

titulo("Até mais!!")