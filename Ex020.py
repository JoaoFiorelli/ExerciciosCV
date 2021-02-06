import random

n1 = input('Aluno um: ')
n2 = input('Aluno dois: ')
n3 = input('Aluno três: ')
n4 = input('Aluno quatro: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de apresentação dos alunos será: ')
print(lista)