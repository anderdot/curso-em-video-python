# Desafio 016: Crie um programa que leia um numero real e mostre na tela sua porção inteira.
from cores import cor
from math import trunc

numero = float(input('Digite um valor: '))
print('A parte inteira é {}{}{}.'.format(cor.verde, trunc(numero), cor.reset))
