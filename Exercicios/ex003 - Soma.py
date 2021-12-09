# Desafio 003: Criei um programa que leia dois números e mostre a soma entre eles.
from cores import cor

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('A soma entre {} e {} é {}{}{}.'.format(n1, n2, cor.verde, soma, cor.reset))
