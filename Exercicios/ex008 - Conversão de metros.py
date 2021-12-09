# Desafio 008: Escreva um programa que leia um valor em metros e exiba convertido 
# em centímetros e milímetros
from cores import cor

metros = float(input('Digite um valor em metros: '))
print('{2} metros é igual a {1}{3:.0f}{0} centímetros ou {1}{4:.0f}{0} milímetros.'.format(
    cor.reset,
    cor.verde,
    metros, 
    metros * 100,
    metros * 1000))
