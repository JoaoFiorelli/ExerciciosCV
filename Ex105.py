def notas(*n,sit=False):
    """
    Calcula várias informações sobre a nota de um dado aluno.
    :param n: Tupla com as notas do aluno.
    :param sit: True se deseja ver em que situação ele está.
    :return: Retorna um dicionário com as infos.
    """

    resumo = {}
    resumo["total"] = len(n)
    resumo["maior"] = max(n)
    resumo["menor"] = min(n)
    resumo["média"] = sum(n)/len(n)

    if sit == True:
        if resumo["média"] < 5:
            resumo["situação"] = "RUIM"
        elif 5 <= resumo["média"] < 7:
            resumo["situação"] = "REGULAR"
        elif resumo["média"] >= 7:
            resumo["situação"] = "BOM"

    return resumo


resposta = notas(2.5, 3.5, 10, 7.4, sit=True)
print(resposta)
help(notas)