# Desafio 017: faça um programa que calcule a hipotenusa digitando o cateto 
# oposto e adjacente de um triângulo retângulo.
from cores import cor
from math import hypot

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
print('A hipotenusa vale {}{:.2f}{}.'.format(
    cor.verde,
    (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2),
    cor.reset))
print('A hipotenusa vale {}{:.2f}{}.'.format(
    cor.verde, 
    hypot(catetoOposto, catetoAdjacente),
    cor.reset))
