from datetime import datetime

dados = {}
dados["nome"] = input("Qual seu nome? ")
dados["nascimento"] = int(input("Qual seu ano de nascimento? "))
dados["idade"] = datetime.now().year - dados["nascimento"]
dados["carteira"] = int(input("Carteira de trabalho (0 não tem): "))

if dados["carteira"] != 0:
    dados["contratação"] = int(input("Ano da contratação: "))
    dados["salario"] = float(input("Salário: "))
    dados["aposentadoria"] = (dados["contratação"] + 35) - dados["nascimento"]

print("-=" * 15)

for k, v in dados.items():
    print(f"-{k} tem o valor {v}!")
