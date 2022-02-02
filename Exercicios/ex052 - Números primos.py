# Desafio 052: Faça um programa que leia um número inteiro e diga se ele é 
# ou não um número primo. 
from cores import cor

numero = int(input('Digite um número: '))
count = 0
print(f'{cor.verde}1', end = ' ')
for i in range(2, numero + 1):
    if numero % i == 0:
        print(f'{cor.verde}', end = '')
        count += 1
    else:
        print(f'{cor.vermelho}', end = '')
    print(f'{i}', end = ' ')
print('\n{0}O número {1}{2}{0} foi divisível {1}{3}{0} vezes, logo {1}{4}{0} primo.'.format(
    cor.reset,
    cor.verde,
    numero, 
    count + 1,
    'é' if count + 1 == 2 else 'não é'
))
