ano = int(input('Descubra se o ano é bissexto digitando ele aqui: '))

if (ano % 4 == 0):
    if (ano % 100 == 0):
        if (ano % 400 == 0):
            print('O ano {} é bissexto!'.format(ano))
        else:
            print('O ano {} não é bissexto!'.format(ano))
    else:
        print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))