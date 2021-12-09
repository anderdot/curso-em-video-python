# Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.
from cores import cor

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
print('Os segmentos acima {}{}{} formar um triângulo.'.format(
    cor.verde,
    'podem' if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 else 'não podem',
    cor.reset))
