# Desafio 042 - Refaça o desafio 035 dos triângulo, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
from cores import cor

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmento acima formam um triângulo', end=' ')
    if r1 == r2 == r3: # n1 == n2 and n2 == 3:
        print(f'{cor.verde}equilátero{cor.reset}.')
    elif r1 != r2 != r3 != r1: #!!!
        print(f'{cor.verde}escaleno{cor.reset}.')
    else: 
        print(f'{cor.verde}isósceles{cor.reset}.')
else:
    print(f'Os segmentos acima {cor.verde}não podem{cor.reset} formar um triângulo.')
