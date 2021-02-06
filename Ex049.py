num = int(input('A tabuada de qual número deseja ver? '))

print("{:=^40}".format('TABUADA'))

for cont in range(0,11):
    print(f"{cont} x {num} = {cont * num}")
