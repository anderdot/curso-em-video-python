# Desafio 077: Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são
# vogais.
from cores import cor

palavras = ('aprender', 'porgramar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'Na palavra {cor.verde}{p:^20}{cor.reset} temos: ', end = f'{cor.verde}')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}', end = ' ')
    print(cor.reset)
