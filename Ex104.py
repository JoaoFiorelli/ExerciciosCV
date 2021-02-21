def leiaint(frase):
    while True:
        num = input(frase)

        if num.isnumeric() == True:
            num = int(num)
            return num
        else:
            print("ERRO, digite um número válido.")

n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")