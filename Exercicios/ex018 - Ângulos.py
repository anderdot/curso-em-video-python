# Desafio 018: Digite unm angulo qualquer e mostre o sen, cos e tan daquele ângulo.
from cores import cor
from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))
radiano = radians(angulo)
print('Seno: {}{:.2f}{}'.format(cor.verde, sin(radiano), cor.reset))
print('Cosseno: {}{:.2f}{}'.format(cor.verde, cos(radiano), cor.reset))
print('Tangente: {}{:.2f}{}'.format(cor.verde, tan(radiano), cor.reset))
