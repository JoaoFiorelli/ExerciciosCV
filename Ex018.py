from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo em graus: '))

s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))

print('Para o ângulo {} o seno é de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}.'.format(ang, s, c, t))