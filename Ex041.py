from datetime import date

atual = date.today().year
nasc = int(input('Qual sua data de nascimento? '))
idade = atual - nasc
print('A data de nascimento do atleta é {} anos!'.format(idade))

if (idade <= 9):
    print('Você está na categoria MIRIM!')
elif (9 < idade <= 14):
    print('Sua categoria é INFANTIL!!')
elif (14 < idade <= 19):
    print('A sua categoria é JUNIOR!!')
elif(19 < idade <= 25):
    print('A sua categoria é SÊNIOR!!')
else:
    print('A sua categoria é MASTER!!')
