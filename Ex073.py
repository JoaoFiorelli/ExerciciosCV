times = ("Internacional", "São Paulo", "Atlético-MG", "Flamengo", "Palmeiras",
         "Grêmio", "Fluminense", "Santos", "Corinthians", "Bragantino",
         "Athletico-PR", "Ceará SC", "Atlético-GO", "Sport Recife", "Bahia",
         "Vasco da Gama", "Fortaleza", "Coritiba", "Goiás", "Botafogo")

print("Os cinco primeiros colocados são: ")
for c in range(0,5):
    print(f"{c+1}º-{times[c]}")
print("=" * 30)

print("Os últimos quatro colocados são: ")
for cont in range(16,20):
    print(f"{cont+1}º-{times[cont]}")
print("=" * 30)

print(f"A lista dos times em ordem alfabética é: ")
for i in range(0,20):
    print(sorted(times)[i])
print("=" * 30)

print(f"A posição do Bragantino na tabela é {times.index('Bragantino')}º lugar")