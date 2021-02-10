aluno = {}
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["media"] = float(input(f"Digite a média das notas do aluno {aluno['nome']}: "))

if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
elif 4 <= aluno["media"] <7:
    aluno["situação"] = "Recuperação"
elif aluno["media"] < 4:
    aluno["situação"] = "Reprovado"

print("-=" * 15)

for k, v in aluno.items():
    print(f"-{k} é igual a {v}!")