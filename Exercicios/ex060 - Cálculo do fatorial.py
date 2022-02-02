# Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex. 5! = 5 * 4 * 3 * 2 * 1 = 120  
from cores import cor

numero = int(input('Digite um número para ver seu fatorial: '))
fatorial = 1

print(f'O cálculo de {cor.verde}{numero}{cor.reset}! é [', end = '')
while numero > 1:                           # Usar o for
    print(f'{numero} x ', end = '')
    fatorial *= numero
    numero -= 1
print(f'1] = {cor.verde}{fatorial}{cor.reset}.')
