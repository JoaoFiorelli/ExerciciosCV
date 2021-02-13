pessoa = {}
galera = []
mulheres = []
maiores = []
soma = 0

while True:
    pessoa["nome"] = input("Nome: ").strip()
    pessoa["sexo"] = input("Sexo [M/F]: ").strip().upper()[0]
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    pessoa.clear()

    desejo = input("Deseja continuar? [S/N]").strip().upper()[0]
    if desejo == "N":
        break

print("-=" * 15)
print(f"-O número total de pessoas cadastradas foi {len(galera)}.")
print(f"-A média de idade foi {soma/len(galera)}.")
for v in galera:
    if v["sexo"] == "F":
        mulheres.append(v["nome"])

    if v["idade"] >= soma/len(galera):
        maiores.append(v["nome"])
print(f"-As mulheres cadastradas foram: {mulheres}")
print(f"-Aqueles que possuem idade maior que a média são: {maiores}")
