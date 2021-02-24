def aumentar(n, porcentagem, formato=False):
    aum = (1 + porcentagem/100) * n
    return aum if formato is False else moeda(aum)


def diminuir(n, porcentagem, formato=False):
    dim = (1 - porcentagem/100) * n
    return dim if formato is False else moeda(dim)


def dobro(n, formato=False):
    dob = 2 * n
    return dob if formato is False else moeda(dob)


def metade(n, formato=False):
    met = n / 2
    return met if formato is False else moeda(met)


def moeda(n, tipo = "R$"):
    return f"{tipo}{n:.2f}".replace(".",",")
