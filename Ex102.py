def fatorial(num, show=False):
    fator = 1
    for i in range(num, 0, -1):
        if show == True:
            if i > 1:
                print(f"{i} x", end=" ")
            elif i == 1:
                print(f"{i} =", end=" ")
        fator *= i
    return fator


print(fatorial(7, show=True))