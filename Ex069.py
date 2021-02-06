totalmaioridade = totalhomem = totalmulhernova = 0

while True:

    idade = int(input("Qual a idade da pessoa cadastrada? "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Qual o sexo da pessoa cadastrada [M/F]? ").strip().upper()[0]

    if idade > 18:
        totalmaioridade += 1

    if sexo == "M":
        totalhomem += 1

    if sexo == "F" and idade < 20:
        totalmulhernova += 1

    desejo = " "
    while desejo not in "SN":
        desejo = input("Deseja prosseguir [S/N}? ").strip().upper()[0]

    if desejo == "N":
        break

print(f"""Foram cadastrados:
-{totalmaioridade} pessoas com mais de 18 anos.
-{totalhomem} homens foram cadastrados.
-{totalmulhernova} mulheres com menos de 20 anos foram cadastradas.""")
