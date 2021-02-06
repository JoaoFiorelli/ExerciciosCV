print("Digite os números que deseja somar. Quando desejar parar digite 999!\n")
n = int(input("Digite um número: "))
soma = cont = 0

while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número: "))

print(f"\nVocê digitou {cont} números e a soma deles é {soma}!!")
print("Programa finalizado!!!")
