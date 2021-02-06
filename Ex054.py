from datetime import date
atual = date.today().year
maiores = 0
menores = 0

for cont in range(1,8):
    nascimento = int(input("Qual o ano de nascimento? "))
    if atual - nascimento >= 18:
        maiores += 1
    else:
        menores += 1

print(f"O número de maiores de idade é {maiores} e o de menores é {menores}!")