from random import randint

PC = randint(0,10)
pessoa = int(input("Qual valor o PC está pensando? "))

while PC != pessoa:
    pessoa = int(input("ERROU! Tente novamente: "))

print(f"ACERTOU!! O computador havia pensado no número {PC}!!!")