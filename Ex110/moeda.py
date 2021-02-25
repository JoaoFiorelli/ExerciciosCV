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


def resumo(n, porcentagemaum, porcentagemdim):
    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)
    print(f"Valor analisado: \t{moeda(n)}")
    print(f"{porcentagemaum}% de aumento: \t{aumentar(n, porcentagemaum, True)}")
    print(f"{porcentagemdim}% de redução: \t{diminuir(n, porcentagemdim, True)}")
    print(f"Dobro do preço: \t{dobro(n, True)}")
    print(f"Metade do preço: \t{metade(n,True)}")
    print("-" * 30)
