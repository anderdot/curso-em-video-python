# Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.
from cores import cor
from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), 
         randint(0, 10), randint(0, 10), )
print(f'{cor.verde}{" Valores Sorteados ":~^40}{cor.reset}')
numeros = ''
for n in range(0, len(tupla)):
    numeros += str(tupla[n]) + (', ' if n < len(tupla)-1 else '.')
print(f'{numeros:^40}')
print(f'{cor.verde}{" Menor Valor Sorteado ":~^40}{cor.reset}')
print(f'{min(tupla):^40}')
print(f'{cor.verde}{" Maior Valor Sorteado ":~^40}{cor.reset}')
print(f'{max(tupla):^40}')
