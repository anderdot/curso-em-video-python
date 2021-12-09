# Desafio 033: faça um programa que leia três números e mostre o maior e menor
from cores import cor

numeros = []
for i in range(0, 3):
    numeros.append(int(input('Digite o {}º número: '.format(i + 1))))
print('O menor valor é {}{}{}.'.format(cor.verde, min(numeros), cor.reset))
print('O maior valor é {}{}{}.'.format(cor.verde, max(numeros), cor.reset))
