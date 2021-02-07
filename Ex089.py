alunos = []
boletim = []

while True:

    alunos.append(input("Digite o nome do aluno: "))
    alunos.append(float(input("Digite a primeira nota: ")))
    alunos.append(float(input("Digite a segunda nota: ")))

    media = (alunos[1] + alunos[2])/ 2
    alunos.append(media)

    boletim.append(alunos[:])
    alunos.clear()

    desejo = input("Deseja continuar? [S/N]").strip().upper()[0]
    if desejo == "N":
        break

print("-=" * 30)
print(f'{"No":^3}{"NOME":^25}{"MÉDIA":^5}')
print("-" * 35)

for aluno in range(0,len(boletim)):
    print(f'{aluno:^3}{boletim[aluno][0]:^25}{boletim[aluno][3]:^5}')

print("-" * 35)

while True:

    desejo = int(input("Deseja ver a nota de algum aluno em específico? [999 interrompe] "))

    if desejo == 999:
        break
    else:
        print(f"As notas de {boletim[desejo][0]} são {boletim[desejo][1]} e {boletim[desejo][2]}.")

print("<<<< VOLTE SEMPRE >>>>")
