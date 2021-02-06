n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if (n1 > n2):
    if (n1 > n3):
        print('O valor {} é o maior.'. format(n1))
        if (n2 > n3):
            print('O valor {} é o menor.'.format(n3))
        else:
            print('O valor {} é o menor.'.format(n2))
    else:
        print('O valor {} é o menor.'.format(n2))
        print('O valor {} é o maior.'.format(n3))
else:
    if (n1 > n3):
        print('O valor {} é o menor.'.format(n3))
        print('O valor {} é o maior.'.format(n2))
    else:
        print('O valor {} é o menor.'.format(n1))
        if (n2 > n3):
            print('O valor {} é o maior.'.format(n2))
        else:
            print('O valor {} é o maior.'.format(n3))
