from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

maior = menor = n[0]

for c in range(0,5):
    if n[c] < menor:
        menor = n[c]

    if n[c] > maior:
        maior = n[c]

print(f"Os valores sorteados foram: {n[0]} {n[1]} {n[2]} {n[3]} {n[4]}")
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")

#------------OUTRO MÉTODO------------
#print(f"O maior número é {max(n)}")
#print(f"O menor número é {min(n)}")