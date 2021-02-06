from datetime import date

ano = int(input('Qual ano você nasceu? '))
atual = date.today().year
idade = atual - ano

tempo = 18 - idade

if (tempo > 0):
    print('''Você ainda não precisa se alistar!!
    Faltam {} anos para que tenha que fazer isso!!'''.format(tempo))
elif (tempo == 0):
    print('Você precisa se alistar esse ano pois tem exatos 18 anos!!')
else:
    print('''Você já deveria ter se alistado!!
    Se tempo de alistamento passou a {} anos!!'''.format(-1 * tempo))
