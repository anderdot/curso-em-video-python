# Desafio 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.
from cores import cor

for i in range(0, 5):
    peso = float(input(f'Digite o peso da {i + 1}ª pessoa: '))
    if i == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {1}{2}{0}kg e o menor {1}{3}{0}kg.'.format(
    cor.reset,
    cor.verde,
    maior,
    menor
))
