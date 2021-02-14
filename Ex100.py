from random import randint


def sorteia(lista):
    for i in range(0,5):
        lista.append(randint(0,50))

    print(f"Os valores sorteados foram: {lista}")

def somaPar(lista, listapar):
    soma = 0
    for i in range(0,5):

        if lista[i] % 2 == 0:
            listapar.append(lista[i])
            soma += lista[i]

    print(f"Os valores pares são {listapar} e a soma deles é {soma}.")


numeros = []
numerospar = []
sorteia(numeros)
somaPar(numeros, numerospar)
