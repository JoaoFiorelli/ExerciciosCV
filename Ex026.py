frase1 = input('Digite uma frase: ').strip()
frase = frase1.lower()

print('A frase acima possui {} letras A.'.format(frase.count('a')))
print('A posição da primeira letra A é: {}'.format(frase.find('a') + 1))
print('A posição da última letra A é: {}'.format(len(frase) - frase[::-1].find('a')))

#print('A posição da primeira letra A é: {}'.format(frase.rfind('a') + 1))